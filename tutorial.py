# # from blessed import Terminal
# # import time
# # import random

# # def start_screen(term):
# #     print("Welcome to the Speed Typing Test!")
# #     print("Press any key to begin...")
# #     term.inkey()

# # def load_text():
# #     with open("text.txt", "r") as f:
# #         lines = f.readlines()
# #         return random.choice(lines).strip()

# # def calculate_wpm(text, time_elapsed):
# #     num_words = len(text.split())
# #     minutes = time_elapsed / 60
# #     if minutes == 0:
# #         return 0
# #     return round(num_words / minutes)

# # def display_text(term, target, current, wpm=0):
# #     typed_text = "".join(current)
# #     # print(term.clear + target)
# #     print(term.clear)
# #     print("WPM:", wpm)
# #     for i, char in enumerate(target):
# #         if i < len(typed_text):
# #             if char == typed_text[i]:
# #                 print(term.green(char), end='', flush=True)
# #             else:
# #                 print(term.red(char), end='', flush=True)
# #         else:
# #             print(char, end='', flush=True)
# #     print()

# # def typing_test(term):
# #     target_text = load_text()
# #     current_text = []
# #     start_time = time.time()

# #     while True:
# #         term.clear()
# #         time_elapsed = max(time.time() - start_time, 1)
# #         wpm = calculate_wpm(target_text, time_elapsed)
# #         display_text(term, target_text, current_text, wpm)

# #         if current_text == list(target_text):
# #             break

# #         key = term.inkey()
        
# #         if key.is_sequence:
# #             if key.name == "KEY_ESCAPE":
# #                 break
# #             elif key.name == "KEY_BACKSPACE":
# #                 if current_text:
# #                     current_text.pop()
# #         else:
# #             current_text.append(key)
    
# #     term.clear()
# #     wpm = calculate_wpm(target_text, time_elapsed)
# #     display_text(term, target_text, current_text, wpm)

# # def main():
# #     term = Terminal()
# #     with term.fullscreen(), term.cbreak(), term.hidden_cursor():
# #         start_screen(term)
# #         typing_test(term)
# #         print("You completed the text! Press any key to continue...")

# # if __name__ == "__main__":
# #     main()


#####################################################################################3

# from blessed import Terminal
# import time
# import random

# def start_screen(term):
#     print("Welcome to the Speed Typing Test!")
#     print("Press any key to begin...")
#     term.inkey()

# def load_text():
#     with open("text.txt", "r") as f:
#         lines = f.readlines()
#         return random.choice(lines).strip()

# def calculate_wpm(text, time_elapsed):
#     num_words = len(text.split())
#     minutes = time_elapsed / 60
#     if minutes == 0:
#         return 0
#     return round(num_words / minutes)

# def display_text(term, target, current, wpm=0):
#     typed_text = "".join(current)
#     print(term.clear)
#     # print("WPM:", wpm)
#     for i, char in enumerate(target):
#         if i < len(typed_text):
#             if char == typed_text[i]:
#                 print(term.green(char), end='', flush=True)
#             else:
#                 print(term.red(char), end='', flush=True)
#         else:
#             print(char, end='', flush=True)
#     print()

# def typing_test(term):
#     target_text = load_text()
#     current_text = []
#     start_time = time.time()

#     while len(current_text) <= len(target_text):
#         term.clear()
#         time_elapsed = max(time.time() - start_time, 1)
#         wpm = calculate_wpm(target_text, time_elapsed)
#         display_text(term, target_text, current_text, wpm)

#         key = term.inkey()
        
#         if key.is_sequence:
#             if key.name == "KEY_ESCAPE":
#                 break
#             elif key.name == "KEY_BACKSPACE":
#                 if current_text:
#                     current_text.pop()
#             elif key.name == "KEY_ENTER":
#                 break
#         else:
#             current_text.append(key)

#     term.clear()
#     wpm = calculate_wpm(target_text, time_elapsed)
#     print("WPM:", wpm)
#     # display_text(term, target_text, current_text, wpm)

#     print("Press any key to continue...")
#     term.inkey()  # Wait for any key press

# def main():
#     term = Terminal()
#     with term.fullscreen(), term.cbreak(), term.hidden_cursor():
#         start_screen(term)
#         typing_test(term)
#         print("You completed the text! Press any key to continue...")

# if __name__ == "__main__":
#     main()



#####################################################################################################


from blessed import Terminal
import time
import random

def start_screen(term):
    print("Welcome to the Speed Typing Test!")
    print("Press any key to begin...")
    term.inkey()

def load_text():
    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def calculate_wpm(num_correct_words, time_elapsed):
    minutes = time_elapsed / 60
    if minutes == 0:
        return 0
    return round(num_correct_words / minutes)

def display_text(term, target, current, wpm=0):
    typed_text = "".join(current)
    print(term.clear)
    # print("WPM:", wpm)
    for i, char in enumerate(target):
        if i < len(typed_text):
            if char == typed_text[i]:
                print(term.green(char), end='', flush=True)
            else:
                print(term.red(char), end='', flush=True)
        else:
            print(char, end='', flush=True)
    print()

def typing_test(term):
    target_text = load_text()
    current_text = []
    start_time = time.time()
    correct_words = 0

    while len(current_text) <= len(target_text):
        term.clear()
        time_elapsed = max(time.time() - start_time, 1)
        wpm = calculate_wpm(correct_words, time_elapsed)
        display_text(term, target_text, current_text, wpm)

        key = term.inkey()
        
        if key.is_sequence:
            if key.name == "KEY_ESCAPE":
                break
            elif key.name == "KEY_BACKSPACE":
                if current_text:
                    current_text.pop()
            elif key.name == "KEY_ENTER":
                break
        else:
            typed_word = ''.join(current_text).split()[-1] if current_text else ''
            typed_text = typed_word + key
            if typed_text == target_text[:len(typed_text)]:
                if typed_text == target_text[:len(typed_text)]:
                    if len(typed_text) == len(target_text) or target_text[len(typed_text)] == ' ':
                        correct_words = len(''.join(current_text).split())

            current_text.append(key)

    end_time = time.time()
    time_elapsed = max(end_time - start_time, 1)
    wpm = calculate_wpm(correct_words, time_elapsed)

    term.clear()
    print("WPM:", wpm)
    print("Time Elapsed (in minutes):", int(time_elapsed / 60))
    print("Number of Correctly Typed Words:", correct_words)

    print("Press any key to continue...")
    term.inkey()  # Wait for any key press

def main():
    term = Terminal()
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        start_screen(term)
        typing_test(term)
        print("You completed the text! Press any key to continue...")

if __name__ == "__main__":
    main()
