from assistant.voice_assistant import run_assistant

if __name__ == "__main__":
    print("=" * 42)
    print("         GT VOICE ASSISTANT")
    print("=" * 42)
    print("1. Voice mode (microphone)")
    print("2. Text mode (type commands)")
    choice = input("Choose mode (1/2): ").strip()

    run_assistant(use_voice=(choice == "1"))
