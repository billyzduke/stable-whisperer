import stable_whisper
import sys
import os

def generate_lyrics_srt(audio_path):
  if not os.path.exists(audio_path):
    print(f"Error: File '{audio_path}' not found.")
    return

  # Load the model. 'base' is fast for testing.
  model = stable_whisper.load_model('base')
  
  print(f"Transcribing {audio_path}... This may take a minute.")
  
  # Transcribe with song-friendly settings
  result = model.transcribe(
    audio_path, 
    vad=True,            # Keep VAD on but...
    demucs=True,         # Use AI to remove instruments (crucial for songs)
    vad_threshold=0.3,   # Lower threshold = more sensitive to quiet singing
    language='en'        # Forcing the language prevents "language switching" bugs
    # , word_timestamps=True)
  ) 

  # Save to SRT format using the same name as the audio file
  output_name = os.path.splitext(audio_path)[0] + ".srt"
  result.to_srt_vtt(output_name)
  print(f"Done! Saved to {output_name}")

if __name__ == "__main__":
  # This grabs the path you provide in the terminal
  if len(sys.argv) > 1:
    target_file = sys.argv[1]
    generate_lyrics_srt(target_file)
  else:
    print("Please provide a path to an audio file.")