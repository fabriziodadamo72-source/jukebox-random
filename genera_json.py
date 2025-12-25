#!/usr/bin/env python3
import os
import json

# Configurazione: cartella -> estensioni da cercare
CONFIG = {
    "mp3": ["mp3"],
    "broadcast": ["mp3"],
    "mp4": ["mp4", "avi", "mov", "webm"]
}

# Mappatura: cartella sorgente -> file JSON di destinazione
MAPPING = {
    "mp3": "content/frasi.json",
    "broadcast": "content/broadcast.json",
    "mp4": "content/video.json"
}

# Per SONG: se vuoi usare la stessa cartella mp3
# oppure crea una cartella "song" separata
SONG_SOURCE = "mp3"  # o "song" se hai cartella dedicata
MAPPING[SONG_SOURCE] = "content/song.json"

def scan_folder(folder, extensions):
    """Scansiona una cartella e ritorna lista di file con estensioni specifiche"""
    if not os.path.exists(folder):
        print(f"⚠️  Cartella '{folder}' non trovata, la salto.")
        return []
    
    files = []
    for file in os.listdir(folder):
        if any(file.lower().endswith(f".{ext}") for ext in extensions):
            files.append(file)
    
    return sorted(files)

def main():
    # Crea cartella content se non esiste
    os.makedirs("content", exist_ok=True)
    
    print("🔍 Scansione cartelle in corso...\n")
    
    for folder, json_path in MAPPING.items():
        extensions = CONFIG.get(folder, ["mp3", "mp4"])
        files = scan_folder(folder, extensions)
        
        if files:
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(files, f, indent=2, ensure_ascii=False)
            print(f"✅ {json_path}: {len(files)} file trovati")
            for file in files[:3]:  # mostra i primi 3
                print(f"   • {file}")
            if len(files) > 3:
                print(f"   ... e altri {len(files)-3}")
        else:
            print(f"❌ {json_path}: NESSUN FILE trovato in '{folder}/'")
        print()
    
    print("✨ JSON generati con successo!\n")

if __name__ == "__main__":
    main()
