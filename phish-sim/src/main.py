import WebsiteCopier
import WebsiteSpoofer
import phishing_email
import tracking_server

def Banner():
    print("-----------------------------------------------------")
    print("|       Welcome to Phishing simulation tool         |")
    print("|                                                   |")
    print("| By: Rameses Peyton, Isha Renner, and Haley Reyes  |")
    print("-----------------------------------------------------")

Banner()

while True:
    print("press 1 to scrape a website")
    print("press 2 to spoof a login page")
    print("press 3 to send a phishing email")
    print("press 4 to run tracking server")
    print("press 5 to exit")
    print(":", end="")
    dec = int(input())

    match dec:
        case 1:
            while True:
                print("press 1 to fetch a url")
                print("press 2 to run the website locally")
                print("press 3 to change the file of the html (default = example.html)")
                print("press 4 to go back")
                print(":", end="")
                dec2 = int(input())
                match dec2:
                    case 1:
                        print("please enter the full url")
                        url = input()
                        WebsiteCopier.fetch(url)
                    case 2:
                        print("starting website locally")
                        WebsiteCopier.run()
                    case 3:
                        print("enter the file Full path/name")
                        inp = input()
                        WebsiteCopier.changefile(inp)
                    case 4:
                        break
                    case _:
                        print("invalid input")
        case 2:
            while True:
                print("press 1 to change the html to a file")
                print("press 2 to run the website locally")
                print("press 3 to reset the html")
                print("press 4 to go back")
                print(":", end="")
                dec2 = int(input())
                match dec2:
                    case 1:
                        inp = input()
                        WebsiteSpoofer.ChangeHTML(inp)
                    case 2:
                        print("starting website locally")
                        WebsiteSpoofer.run()
                    case 3:
                        WebsiteSpoofer.ResetHTML()
                        print("html reset to default")
                    case 4:
                        break
                    case _:
                        print("invalid input")
        case 3:
            print("press 1 to send a phishing email")
            print("press 2 to go back")
            print(":", end="")
            dec2 = int(input())

            if dec2 == 1:
                print("Enter your email address: ")
                sender_email = input()
                print("Enter your email app-specific password: ")
                password = input()
                print("Enter the target's email address: ")
                receiver_email = input()
                print("Enter the subject of the phishing email: ")
                subject = input()
                print("Enter the body content of the phishing email (HTML format): ")
                body = input()
                print("Enter the URL for tracking (e.g., http://localhost:5000/track_click): ")
                tracking_url = input()

                phishing_email.send_phishing_email(sender_email, password, receiver_email, subject, body, tracking_url)
            elif dec2 == 2:
                continue
            else:
                print("invalid input")
        case 4:
            print("Starting tracking server...")
            tracking_server.app.run(host='0.0.0.0', port=5000)
        case 5:
            print("Exiting...")
            break
        case _:
            print("invalid option")
