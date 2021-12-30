
import PySimpleGUI as sg
import os, clipboard, time

os.system('cls')

def english_to_arabic(inp):
    sakinable = ['b','t','c','j','H','Q','d','z','r','Z','s','S','C','D','T','J',  '`',  'g','f',  'q','K',  'k','l','m','n','w','h','\'', '\"', '|','y']
    consonants = ['*','\'', '\"', '|', '`','a','A',  'E',   'b',  'c','C',  'd','D',  'f',  'g',  'h','H',  'j','J',  'k','K',  'l',     'm',  'n',  'q','Q',  'r',  's','S',  't','T',  'w','W',  'y','Y',  'z','Z']
    arabic=''
    i=0
    if inp == '':
        return ''
    while i < len(inp):
        next = ''
        next2 = ''
        next3 = ''
        next4 = ''
        prev = ''
        arabic_prev = ''
        prev2 = ''
        arabic_prev2 = ''
        prev3 = ''
        ginipig = inp[i]
        if i+1 < len(inp):
            next = inp[i+1]
        if i+2 < len(inp):
            next2 = inp[i+2]
        if i+3 < len(inp):
            next3 = inp[i+3]
        if i+4 < len(inp):
            next4 = inp[i+4]
        if i != 0:
            prev = inp[i-1]
        if i > 1:
            prev2 = inp[i-2]
        if i > 2:
            prev3 = inp[i-3]
        
        if len(arabic) >= 1:
            arabic_prev = arabic[len(arabic)-1]
        if len(arabic) >= 2:
            arabic_prev2 = arabic[len(arabic)-2]
        if len(arabic) >= 3:
            arabic_prev3 = arabic[len(arabic)-3]
        
        if ginipig == ' ':
            arabic += ' '
        elif ginipig == '\n':
            arabic += '\n'
        
        elif ginipig == '1':
            arabic += '١'
        elif ginipig == '2':
            arabic += '٢'
        elif ginipig == '3':
            arabic += '٣'
        elif ginipig == '4':
            arabic += '٤'
        elif ginipig == '5':
            arabic += '٥'
        elif ginipig == '6':
            arabic += '٦'
        elif ginipig == '7':
            arabic += '٧'
        elif ginipig == '8':
            arabic += '٨'
        elif ginipig == '9':
            arabic += '٩'
        elif ginipig == '0':
            arabic += '٠'
        elif ginipig == '%':
            arabic += '٪'
        elif ginipig == '?':
            arabic += '؟'
        
        

        elif ginipig == 'b':
            arabic += 'ب'
        elif ginipig == 't':
            if next != 'w':
                arabic += 'ة'
            else:
                arabic += 'ط'
                i += 1
                if i+1 < len(inp):
                    next = inp[i+1]
                if i+2 < len(inp):
                    next2 = inp[i+2]
                if i+3 < len(inp):
                    next3 = inp[i+3]
                if i+4 < len(inp):
                    next4 = inp[i+4]
        elif ginipig == 'T':
            arabic += 'ت'
        elif ginipig == 'c':
            arabic += 'ث'
        elif ginipig == 'j':
            arabic += 'ج'
        elif ginipig == 'H':
            arabic += 'ح'
        elif ginipig == 'Q':
            arabic += 'خ'
        elif ginipig == 'd':
            arabic += 'د'
        elif ginipig == 'z':
            arabic += 'ذ'
        elif ginipig == 'r':
            arabic += 'ر'
        elif ginipig == 'Z':
            arabic += 'ز'
        elif ginipig == 's':
            arabic += 'س'
        elif ginipig == 'S':
            arabic += 'ش'
        elif ginipig == 'C':
            arabic += 'ص'
        elif ginipig == 'D':
            arabic += 'ض'
         #elif ginipig == 'T': arabic += 'ط'""" ---- used before in another form
        elif ginipig == 'J':
            arabic += 'ظ'
        elif ginipig == '`':
            arabic += 'ع'
        elif ginipig == 'g':
            arabic += 'غ'
        elif ginipig == 'f':
            arabic += 'ف'
        elif ginipig in ['q','K']:
            arabic += 'ق'
        elif ginipig == 'k':
            arabic += 'ك'
        elif ginipig == 'l':
            arabic += 'ل'
        elif ginipig == 'm':
            arabic += 'م'
        elif ginipig == 'M':
            arabic += 'ۘ' # ওয়াকফে লাযিম
        elif ginipig == 'n':
            arabic += 'ن'
        elif ginipig == 'w':
            arabic += 'و'
        elif ginipig == 'W':
            arabic += 'ؤ'
        elif ginipig == 'h':
            arabic += 'ه'
        elif ginipig == '\'' and prev != '\\':
            if (next not in ['',' ','\n']) and (next not in ['a','A','u','U','i','I'] or next2 not in ['',' ','\n']) and (next not in ['a','i','u'] or next2 != 'N' or next3 not in ['',' ','\n']): # যদি শেষ হামযা না হয়
                if prev == 'l':
                    arabic += 'أ'
                elif arabic_prev == 'ْ' and arabic_prev2 != 'و' and next not in ['',' ','\n']:# আগেরটায় و ছাড়া অন্য কিছুতে সাকিন
                    if next in ['u','U']:
                        arabic += 'ؤ'
                    elif next in ['a','A']:
                        arabic += 'أ'
                    elif next in ['i','I']:
                        arabic += 'ئ'
                elif arabic_prev == 'ا' and arabic_prev2 == 'َ' and next in ['u'] and next2 != 'w': # for طَاؤُط but not for طَاءُوط
                    arabic += 'ؤ'
                elif arabic_prev == 'ْ' and arabic_prev2 == 'و' and arabic_prev3 in ['ٗ','ُ','ٰ','َ']: #[পেশ, উল্টা পেশ, খাড়া যবর, যবর] ---- for طَوْءِ	طَوْءُط	طَوْءَط	طَوْءِيط طَوْءُوط طَوْءَاط and طُوءِط طُوءُط طُوءَط	طُوءِيط	طُوءُوط	طُوءَاط
                    arabic += 'ء'
                elif arabic_prev in ['ِ','ٖ'] or (arabic_prev == 'ْ' and arabic_prev2 == 'ي') or next in ['i','I']: # for طِئِط	طِئُط طِئَط طِئِيط طِئُوط طِئَاط and طَئِيط طَئِط
                    arabic += 'ئ'
                elif arabic_prev in ['ٗ','ُ']:
                    if next not in  ['i','I']: # for طُؤُط طُؤَط طُؤُوط طُؤَاط
                        arabic += 'ؤ'
                elif arabic_prev == 'َ': # for أَنْشَأْنَا (in Waaqiyah)
                    arabic += 'أ'
                else:
                    arabic += 'ء'
            elif prev in ['', ' ', '\n']: # initial Hamza
                if next in ['a','u','A','U']:
                    arabic += 'أ'
                elif next in ['i','I']:
                    arabic += 'إ'
                else:
                    arabic += 'ء'

            elif next in ['',' ','\n'] or (next in ['a','A','i','I','u','U'] and next2 in ['',' ','\n']) or (next in ['a','i','u'] and next2 == 'N' and next3 in ['',' ','\n']): # final hamza
                if arabic_prev in ['ٗ','ُ']:
                    arabic += 'ؤ'
                elif arabic_prev in ['َ','ٰ']:
                    arabic += 'أ'
                elif arabic_prev in ['ٖ','ِ']:
                    arabic += 'ئ'
                else:
                    arabic += 'ء'
                                                  #if prev in ['i','I','y'] and next not in ['',' ','\n'] and (next not in ['a','A','u','U','i','I'] and next2 not in ['',' ','\n']):
            else:
                arabic += 'ء'
        elif ginipig == '|' and prev != '\\':
            arabic += 'ء'
        elif ginipig == '\"' and prev != '\\':
            arabic += 'ئ'
        elif ginipig == 'y':
            arabic += 'ي'
        elif ginipig == 'Y':
            arabic += 'ى'
        
        elif ginipig == 'a':
            if (prev in ['',' ','\n'] and next != '~') or (arabic_prev == 'ِ' and arabic_prev2 == 'ب') or (arabic_prev == 'َ' and arabic_prev2 == 'ف'):
                arabic += 'ٱ'
            else:
                arabic += 'ا'
        elif ginipig == 'A':
            arabic += 'أ'
            if next != 'a': # পরে আরেকটা a না থাকলে যবর লাগিয়ে দাও
                arabic += 'َ'
        elif ginipig == 'I':
            arabic += 'إِ'
        elif ginipig == 'U':
            arabic += 'أُ'
        elif ginipig == 'i':
            arabic += 'ٱؚ'
        elif ginipig == 'u':
            arabic += 'ٱؙ'

        elif ginipig == '\\':
            if next == '\\':
                arabic += '\\'
                i += 1
            else:
                arabic += ''

        elif ginipig == '^':
            arabic += 'ْ' # জযম
        elif ginipig == '*':
            arabic += 'ّ' # তাশদীদ
        elif ginipig == '~':
            arabic += 'ٓ'

        elif ginipig not in ['N']: # কিছুর সাথে না মিললে যা আছে তাই দিয়ে দাও
            if not (ginipig == '_' and prev != '\\'):
                arabic += ginipig

        if (ginipig in sakinable and (next in sakinable or next in ['\n',' ',''])) and (ginipig != next) and prev not in ['',' ','\n','\\'] and arabic_prev != 'ْ': # Automatic Jazam
            if ginipig not in ['l','n','m','w']:
                arabic += 'ْ' # জযম
            elif ginipig == 'l':
                qamariyya = ['b','g','H','j','k','w','Q','f','`','q','K','\'','y','m','h',' ']
                if next in qamariyya or (next == ' ' and next2 in qamariyya) or next in ['','\n']:
                        arabic += 'ْ' # জযম
                else:
                    arabic += ''
            elif ginipig == 'n':
                idgaam_nun = ['y','Y','r','m','l','w','n']
                if next in idgaam_nun or (next == ' ' and next2 in idgaam_nun):
                    if next in ['y','w'] and next2 == 'a' and next3 == 'N': # ইযহারে মত্বলক
                        arabic += 'ْ'
                    else:
                        arabic += ''
                elif next == 'b' or (next == ' ' and next2 == 'b'): # min ba`di
                    arabic += ' ۘ '
                else:
                    arabic += 'ْ'
            elif ginipig == 'm':
                if next == 'm' or (next == ' ' and next2 == 'm'):
                    arabic += ''
                else:
                    arabic += 'ْ'
            elif ginipig == 'w':
                if arabic_prev2 in ['أ','ا'] and arabic_prev == 'ُ' and next == 'l': # for أُولٰٓإِكَ ('ulaa'ika)
                    arabic += ''
                else:
                    arabic += 'ْ'


        if (ginipig == next) and (' ' not in next) and next not in ['', ' ', '\n', '\\', '\'', 'a', 'A', 'E', 'i', 'u', 'I', 'U'] and prev != '\\': # Automatic Tashdeed
            if ((prev2 in ['', ' ','\n'] and prev == 'a') or (prev2 == 'a' and prev == '~')) and ginipig == 'l' and next2 in ['a','A'] and next3 == 'h': # for 'اللّٰهُ' word
                arabic += 'ل'
                arabic += 'ّ' # তাশদীদ
                arabic += 'ٰ' # খাড়া যবর
                i += 2
            else:
                arabic += 'ّ' # তাশদীদ
                i += 1
                if i+1 < len(inp):
                    next = inp[i+1]
                if i+2 < len(inp):
                    next2 = inp[i+2]




        
        if ginipig not in [' ','\n']:
            if  ginipig in consonants:
                if next == 'a':
                    if next2 == 'N':
                        arabic += 'ً' # দুই যবর
                        if next3 in ['',' ','\n'] and ginipig not in ['t','|']: # automatic alif after দুই যবর in the last position (beta)
                            arabic += 'ا'
                    else:
                        arabic += 'َ' # যবর
                    i += 1
                elif  next == 'A':
                    arabic += 'ٰ' # খাড়া যবর
                    i += 1
                elif next == 'i':
                    if next2 == 'N':
                        arabic += 'ٍ' # দুই যের
                    else:
                        arabic += 'ِ' # যের
                    i += 1
                elif next == 'I':
                    arabic+= 'ٖ' # খাড়া যের
                    i += 1
                elif next == 'u':
                    if next2 == 'N':
                        arabic += 'ٌ' # দুই পেশ
                    else:
                        arabic += 'ُ' # পেশ
                    i += 1
                elif next == 'U':
                    arabic+= 'ٗ' # উল্টা পেশ
                    i += 1


        i+=1

    return arabic







sg.theme('DarkBlue')
   
layout = [[sg.Text(text='Type the phonetic form in English:', text_color='White', font=('Times', 16))],
        [sg.Multiline(key='-IN-', text_color='Pink', disabled=False,focus=True, font=('Times', 14), size=(200, 7))],
        [sg.Text(text='Arabic:', text_color='Yellow', font=('Times', 18))],
        [sg.Multiline(key='-OUTPUT-', text_color='White',disabled=True, font=('Times', 22), size=(180,100), autoscroll=True)]]


window = sg.Window('Arabic Phonetic Output by KMFRuhan', layout, size=(600,450), resizable=True, location=(160,100), keep_on_top = False, return_keyboard_events=True, finalize=True)

window.bind("<Control-KeyPress-w>", "ctrl-w")
window.bind("<Control-KeyPress-W>", "ctrl-w")
window.bind("<KeyPress>", "KP")
window.bind("<Control-KeyPress-c>", "ctrl-c")
window.bind("<Control-KeyPress-C>", "ctrl-c")

# Enable the undo mechanism:
text = window['-IN-'].Widget
text.configure(undo=True)



while True:
    event, values = window.read()

    if event in  (None, 'ctrl-w'):
        break

    if event == 'KP':
        result = english_to_arabic(values['-IN-'])
        window['-OUTPUT-'].update(result)
    
    
    if event == "ctrl-c":
        clipboard.copy(result)

window.close()

os.system('cls')