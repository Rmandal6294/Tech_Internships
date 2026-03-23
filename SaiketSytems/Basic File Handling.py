# ========================= Basic File Handling in Python =========================
import re
print("""
      =======================================================================
                        📂  Basic File Handling  📂
      =======================================================================
    """)

print(""" 🚀 Features: 
      1. Read Data From a Text File.
      2. Write Into a Text File
      3. Find Word From a Text File
      4. Replacing Specific Words.
      5. Exit The Program.
""")

def read_fileData(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            content = f.read()
            print("📊 The file content is:=====>\n")
            print(content)
    except FileNotFoundError:
        print("⚠️ File Not Found")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        
def write_fileData(file_name, Userdata):
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(Userdata)
            print("✅ File written successfully.")
    except Exception as e:
        print(f" ❌ An Error Occurred: {e}")
        
def find_word(file_name, finding_word):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            text = f.read().lower()
            count = re.findall(rf"\b{finding_word}\b", text, re.IGNORECASE)
            print(f"✔️ '{finding_word}' appears {len(count)} times")
    except FileNotFoundError:
        print("⚠️File not Found")
    except Exception as e:
        print(f"❌ An Error Occurred: {e}")
        
def replace_word(file_name, old_word, new_word):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            text = f.read().lower()
        text = re.sub(rf"\b{old_word}\b", new_word, text, flags=re.IGNORECASE)
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"✅ Replaced '{old_word}' with '{new_word}' successfully.")
    except FileNotFoundError:
        print("⚠️ File not Found")
    except Exception as e:
        print(f"❌ An Error Occurred: {e}")
        

while True:
    print("============================= || ==============================")
    choice = int(input("🎯 What you want to do (choose: 1-5): "))
    filename = input("\n🗃️  Enter the Filename: ")
    
    if choice == 1:
        read_fileData(filename)
    elif choice == 2:
        contentData = input("📊 Enter you Data: ")
        write_fileData(filename, contentData)
    elif choice == 3:
        word = input("👀 Enter the 'word' you want to find: ")
        find_word(filename, word)
    elif choice == 4:
        oldWord = input("✈️ Enter the 'word' you want to change: ")
        newWord = input("✈️ Enter the ' New word': ")
        replace_word(filename, oldWord, newWord)
    elif choice == 5:
        print("👋 ======= GoodBy ========== 👋")
        break
    else:
        print("⚠️ Enter Between 1 t0 5")
        
        