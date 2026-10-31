# Mouse Mover Python Script (macOs only)

### Stay active even when you are away

---

## Nudges your mouse every so often so Teams keeps you green while you're away. Press any key to stop it.

Yo!

I was looking for a software that kept me active on Teams, but could not find anything good or trustworthy.
So, I thought I'd create one.
_Claude told me I wrote some problematic shit here, so I removed it._ :\

This is not polished, but does the job and I will be improving it later.

But no promises.

**Heads up:** I made this for my own machine. If you want to use it on a work device, check your workplace rules first.

## Steps

1. Install Python. Homebrew is the easiest, but you can install it however you want.
2. Either download the repo, or copy `script.py` into VS Code and save it.
3. Navigate to that folder/repo from the terminal and paste `python3 -m venv .venv`. This creates a `.venv` folder.
4. Paste and enter `source .venv/bin/activate` in the same terminal.
5. Paste and enter `python3 -m pip install pynput` in the same terminal. This installs pynput.
6. Open the repo folder in VS Code (you might need to install the Python extension if you haven't already). If the venv isn't picked up, press Cmd+Shift+P → "Python: Select Interpreter" and choose the one with `.venv` in it.
7. Try running the script. You will get an error saying something like VS Code does not have permissions.
8. Click the popup and open Settings through it. It will take you straight to the right privacy settings.
9. Enable Input Monitoring and Device and Data Control for VS Code and Terminal. I just do it this way because it is a bitch to find the right setting.
10. Try running the script again.
11. It should move your mouse. Press any key to stop it.
12. Now, from the VS Code terminal, type `which python` and copy the output _(it should end in `.venv/bin/python`)_.
13. On your desktop, or wherever you want to run the script from, create a new text file and paste the output.
14. Press space, then paste the path of `script.py` on the same line.
15. It should look something like this (one space between the two paths):

    ```
    /Users/yourUsername/.../mouseMoverScript/.venv/bin/python /Users/yourUsername/.../mouseMoverScript/script.py
    ```

    > There is a space " " between two paths.

16. Save the text file as `mouseMover.command`. You can name it whatever you want, but it has to end in `.command`.
17. Open Terminal, type `chmod +x ` (with a space at the end), then paste the path of the `.command` file. You can also drag the file into the terminal.
18. Press Enter.
19. And voilà, you have a working mouse mover set-up.
20. Give it a try, I dare you.

You can now run the mouse mover by opening the `.command` file.

## Notes

- I run Caffeine, so my device is awake all the time. If you don't, your Mac might go nighty night before Teams even marks you as away. The mouse movement might keep it awake on its own, but I haven't tested that yet. Will update once I do.
- venv is a virtual environment for Python. Please google it for more info.
- pynput is a third-party library that lets Python control the mouse and keyboard.
- Whatever key you press to stop the program gets typed. Please check where it landed.

## Device Info

- MacBook Air M2
- macOS Golden Gate 27.0.1
- Python 3.15.2
