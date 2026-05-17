import json
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
import os
import subprocess

def get_hardware_telemetry():
    """Prikuplja telemetrijske podatke nativno (Android/Termux kompatibilno)."""
    try:
        load1, load5, load15 = os.getloadavg()
        cpu_cores = os.cpu_count() or 8
        cpu_util = round((load1 / cpu_cores) * 100, 2)
    except Exception:
        cpu_util = 0.0

    mem_percent = 0.0
    try:
        with open('/proc/meminfo', 'r') as f:
            lines = f.readlines()
            total = free = 0
            for line in lines:
                if 'MemTotal:' in line:
                    total = int(line.split()[1])
                elif 'MemAvailable:' in line:
                    free = int(line.split()[1])
            if total > 0:
                mem_percent = round(((total - free) / total) * 100, 2)
    except Exception:
        pass

    return {
        "cpu_utilization_percent": cpu_util,
        "memory_usage_percent": mem_percent,
        "active_threads": os.cpu_count() or 8
    }

def generate_m2m_transcript(nickname_raw, legacy_projects):
    """Generira M2M payload uz integraciju telemetrije s nultom entropijom."""
    clean_identifier = nickname_raw.replace("✨-", "").replace("-♾️", "")
    
    m2m_payload = {
        "m2m_node": {
            "device_id": f"NODE-{clean_identifier.upper()}",
            "environment": "Super_Node_0_Termux_Native",
            "profile": {
                "raw_nickname": nickname_raw,
                "alphanumeric_id": clean_identifier,
            },
            "telemetry": get_hardware_telemetry(),
            "timestamp_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "legacy_transcripts": []
        }
    }
    
    for index, proj in enumerate(legacy_projects, start=1):
        transcript_entry = {
            "sequence_id": f"TX-{clean_identifier}-{index:04d}",
            "project_name": proj.get("name"),
            "status": proj.get("status", "ARCHIVED"),
            "checksum": hex(hash(proj.get("name")) & 0xffffffff)
        }
        m2m_payload["m2m_node"]["legacy_transcripts"].append(transcript_entry)
        
    return m2m_payload

# --- EXECUTION ENGINE ---
if __name__ == "__main__":
    NICKNAME = "✨-bis3946-♾️"
    PROJECTS_DATA = [
        {"name": "NuN Project", "status": "COMPLETED"},
        {"name": "Ana AGI Core", "status": "DEPRECATED"}
    ]
    
    json_data = generate_m2m_transcript(NICKNAME, PROJECTS_DATA)
    
    json_filepath = "m2m_payload.json"
    with open(json_filepath, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)
        
    print("--- [S25 ULTRA] NATIVNA LOKALNA TELEMETRIJA (JSON) ---")
    print(json.dumps(json_data, indent=2, ensure_ascii=False))
