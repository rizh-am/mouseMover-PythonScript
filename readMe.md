# Mouse Mover Python Script (Mac)

### Stay active even when you are away

Yo!

I was looking for a software that kept me active on Teams, but could not find anything good or trustworthy.
So, I thought I'd create one.
Claude told me I wrote some problematic shit here, so I removed it. :\

This is not polished, but does the job and I will be improving it later.

But no promises.

## Steps

1. Install python. Homebrew is the easiest. You can install however you want
2. Either download the repo, or copy the script.py into VSCode and save it.
3. Install VENV on that folder
4. Install pynput. (it is a third party library that enables mouse and keyboard integration? with python)
5. Try running the script through VSCode (You might need to install the Python extension if you haven't already)
6. You will get an error saying something like VSCode does not have permissions.
7. Click the window, and open settings through it. It will take you straight to the target privacy settings.
8. Enable Input Monitoring and Device and Data Control for VSCode and Terminal. I just do it this way because it is a bitch to find the right setting
9. Try running the script
10. it should move your mouse, press a keyboard key to stop it.
11. Now, from the VSCode Terminal, type which python, and copy the output
12. On your desktop, or wherever you want the script to run from, create a new text file, and paste the output.
13. press space, and paste the path of the script.py on the text file.
14. It should be something like {$VENV Path} + " " + {$Script Path}
15. save the text file as "mouseMover.command" you can save it as whatever you want, but the filename should end with .command
16. open terminal and type "chmod +x " and paste the command file path here. You can also drag the file to the terminal
17. press enter
18. and viola, you have a working mouse mover set-up
19. give it a try, I dare you

You can now run the mouse mover by opening the command file.
Please note that I run caffeine, so my device is awake all the time, if you have different, you might have to find a solution for that.
Like your device might go nighty night before you are even inactive on teams.
I think because of the mouse movement, the device should keep awake, but I have not tested it yet.
Will update once I do
