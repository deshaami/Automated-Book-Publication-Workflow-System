# editor.py

def human_review_loop(text):
    print("\n✅ AI Reviewed Content:\n")
    print(text)

    while True:
        decision = input("\nDo you want to (e)dit, (a)ccept or (r)eject? [e/a/r]: ").strip().lower()
        if decision == 'e':
            edited = input("\n📝 Enter your edited version:\n")
            text = edited
        elif decision == 'a':
            print("\n✅ Final approved version saved.\n")
            
            # Save version here after acceptance
            from version_manager import save_version
            save_version("Alice’s Adventures", text)
            
            return text
        elif decision == 'r':
            print("\n❌ Rejected. Re-entering review loop.\n")
        else:
            print("⚠️ Invalid option. Try again.")

if __name__ == "__main__":
    from reviewer import review_text
    
    raw = input("📄 Enter raw text to review: ")
    reviewed = review_text(raw)
    final_version = human_review_loop(reviewed)
    
    print("\n🎉 Final Output:\n", final_version)
