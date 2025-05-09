import WebsiteCopier
import WebsiteSpoofer
import phishing_email
import tracking_server
import threading

def Banner():
    print("-----------------------------------------------------")
    print("|       Welcome to Phishing simulation tool         |")
    print("|                                                   |")
    print("| By: Rameses Peyton, Isha Renner, and Haley Reyes  |")
    print("-----------------------------------------------------")

def run_tracking_server():
    """Function to run the tracking server in a separate thread."""
    tracking_server.app.run(host='0.0.0.0', port=5000)

# Start tracking server in a separate thread
tracking_thread = threading.Thread(target=run_tracking_server)
tracking_thread.daemon = True  # Daemonize thread to terminate with main program
tracking_thread.start()

Banner()

while(True):
    
    
    print("press 1 to scrape a website")
    print("press 2 to spoof a login page")
    print("press 3 to go to phishing email")
    print("press 4 to go to tracking server")
    print(":",end="")
    dec = int(input())
    
    match dec:
        case 1:
            while (True):
                print("press 1 to fetch a url")
                print("press 2 to run the website locally")
                print("press 3 to change your website dir (default template Login_v4)")
                print("press 4 to change the base HTML")
                print("press 5 to go back")
                print(":",end="")
                dec2 = int(input())
                match dec2:
                    case 1:
                        print("please enter the full url")
                        print(":",end="")
                        url = input()
                        WebsiteCopier.fetchUrl(url)
                        break
                    case 2:
                        print("starting website locally")
                        WebsiteCopier.run()
                        break
                        
                    case 3:
                        print("enter the file Full path/name")
                        print(":",end="")
                        inp = input()
                        WebsiteCopier.changewebsiteDir(inp)
                        break
                    case 4:
                        print("enter the file name of html")
                        print(":",end="")
                        inp = input()
                        WebsiteCopier.changewebsiteBase(inp)
                        break
                    case 5:
                        break
                    case _:
                        print("invalid input")
                
            
            
        case 2:
            print("press 1 to change the html to a file")
            print("press 2 to run the website locally")
            print("press 3 to change your website dir (default template Login_v4)")
            print("press 4 to go back")
            print(":",end="")
            dec2 = int(input())
            match dec2:
                case 1:
                    print(":",end="")
                    inp = input()
                    WebsiteSpoofer.changewebsiteBase(inp)
                    break
                
                case 2:
                    print("starting website locally")
                    print(":",end="")
                    WebsiteSpoofer.run()
                    break
                
                case 3:
                    print("enter the file Full path/name")
                    print(":",end="")
                    inp = input()
                    WebsiteSpoofer.changewebsiteDir(inp)
                    
                    break
                case 4:
                    break
                case _:
                    print("invalid input")
        case 3:
            # Handle phishing email
            print("press 1 to send a phishing email")
            print("press 2 to go back")
            print(":", end="")
            dec2 = int(input())

            if dec2 == 1:
                # Gather email details from the user
                print("Enter your email address: ")
                sender_email = input()
                print("Enter your email app-specific password: ")
                password = input()
                print("Enter the target's email address: ")
                receiver_email = input()

                # Gather subject and body content for email
                print("Enter the subject of the phishing email: ")
                subject = input()

                print("Enter the body content of the phishing email (HTML format): ")
                body = input()

                print("Enter the URL for tracking (e.g., http://localhost:5000/track_click): ")
                tracking_url = input()

                # Call the function to send the phishing email with user-configured values
                phishing_email.send_phishing_email(sender_email, password, receiver_email, subject, body, tracking_url)
            elif dec2 == 2:
                break
            else:
                print("invalid input")
        case 4:
            print("Going to tracking server...")
            break
        case _:
            print("invalid option")
