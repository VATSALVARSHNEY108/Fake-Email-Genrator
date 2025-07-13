try:
    import random, string, os, sys, names, time, requests, json
    from rich.console import Console
    from rich.panel import Panel
    from mimesis.locales import Locale
    from faker import Faker
    from mimesis import Person
    from rich import print as printf
    from randomuser import RandomUser
except ModuleNotFoundError as e:
    sys.exit(f"[Error] {str(e).capitalize()}!")

LIVE, LOOPING, DIE, UNKNOWN = [], 0, [], []

class FITUR:
    def __init__(self) -> None:
        pass

    def UTAMA(self):
        try:
            self.TAMPILKAN_LOGO()
            printf(
                Panel(
                    f"""[bold green]01[bold white]. Create Email from Random String
[bold green]02[bold white]. Create Email from Mimesis
[bold green]03[bold white]. Create Email from Faker
[bold green]04[bold white]. Create Email from Names
[bold green]05[bold white]. Create Email from RandomUser
[bold green]06[bold white]. Valid Email Checker
[bold green]07[bold white]. Exit""",
                    style="bold bright_black",
                    width=59,
                    title="[bold bright_black]> [Main Menu] <",
                    subtitle="[bold bright_black]╭───────",
                    subtitle_align="left",
                )
            )
            CHOOSE = Console().input("[bold bright_black]   ╰─> ")
            if CHOOSE in ["1", "2", "3", "4", "5", "01", "02", "03", "04", "05"]:
                printf(
                    Panel(
                        f"[bold white]Enter a domain (e.g., [bold green]@gmail.com[bold white]). Only one domain allowed!",
                        style="bold bright_black",
                        width=59,
                        title="[bold bright_black]> [Domain] <",
                        subtitle="[bold bright_black]╭───────",
                        subtitle_align="left",
                    )
                )
                self.DOMAIN = Console().input("[bold bright_black]   ╰─> ")
                if "@" in str(self.DOMAIN) and "." in str(self.DOMAIN):
                    printf(
                        Panel(
                            f"[bold white]Enter number of emails to generate (min [bold green]100[bold white]):",
                            style="bold bright_black",
                            width=59,
                            title="[bold bright_black]> [Count] <",
                            subtitle="[bold bright_black]╭───────",
                            subtitle_align="left",
                        )
                    )
                    self.COUNT = int(Console().input("[bold bright_black]   ╰─> "))
                    if self.COUNT >= 100:
                        printf(
                            Panel(
                                f"[bold white]Generating emails... Press [bold green]CTRL + C[bold white] to stop safely.",
                                style="bold bright_black",
                                width=59,
                                title="[bold bright_black]> [Note] <",
                            )
                        )
                        self.FILE_NAME = EMAILS().GENERATE_RANDOM_FILENAME()
                        method = {
                            "1": EMAILS().RANDOM_STRING,
                            "2": EMAILS().MIMESIS,
                            "3": EMAILS().FAKER,
                            "4": EMAILS().NAMES,
                            "5": EMAILS().RANDOM_USER,
                        }[CHOOSE.lstrip("0")]
                        self.STATUS = method(self.DOMAIN, self.COUNT, self.FILE_NAME)
                        if self.STATUS:
                            printf(
                                Panel(
                                    f"[bold white]Emails saved to [bold green]{self.FILE_NAME}",
                                    style="bold bright_black",
                                    width=59,
                                    title="[bold bright_black]> [Success] <",
                                )
                            )
                        else:
                            printf(
                                Panel(
                                    f"[bold red]Failed to generate emails.",
                                    style="bold bright_black",
                                    width=59,
                                    title="[bold bright_black]> [Failure] <",
                                )
                            )
                        sys.exit()
                    else:
                        printf(
                            Panel(
                                f"[bold red]Please generate at least 100 emails!",
                                style="bold bright_black",
                                width=59,
                                title="[bold bright_black]> [Error] <",
                            )
                        )
                        sys.exit()
            elif CHOOSE in ["6", "06"]:
                printf(
                    Panel(
                        f"[bold white]Enter the file name to check (e.g., [bold green]example.txt[bold white])",
                        style="bold bright_black",
                        width=59,
                        title="[bold bright_black]> [Check Emails] <",
                        subtitle="[bold bright_black]╭───────",
                        subtitle_align="left",
                    )
                )
                self.FILE_NAME = Console().input("[bold bright_black]   ╰─> ")
                if os.path.exists(self.FILE_NAME):
                    lines = open(self.FILE_NAME, "r").readlines()
                    if len(lines) >= 1:
                        self.SAVE_FILES = EMAILS().GENERATE_RANDOM_FILENAME().replace(".txt", "")
                        self.FILE_LIVE = f"{self.SAVE_FILES}_Live.txt"
                        self.FILE_DIE = f"{self.SAVE_FILES}_Die.txt"
                        printf(
                            Panel(
                                f"[bold white]Checking emails... this may take a few minutes.",
                                style="bold bright_black",
                                width=59,
                                title="[bold bright_black]> [Processing] <",
                            )
                        )
                        for EMAIL in lines:
                            try:
                                CHECKER().EMAIL([EMAIL.strip()], self.FILE_LIVE, self.FILE_DIE)
                            except KeyboardInterrupt:
                                break
                        printf(
                            Panel(
                                f"[bold white]Finished: [bold green]{len(LIVE)}[bold white] live / [bold red]{len(DIE)}[bold white] dead emails.",
                                style="bold bright_black",
                                width=59,
                                title="[bold bright_black]> [Done] <",
                            )
                        )
                    else:
                        printf(
                            Panel(
                                f"[bold red]File is empty. Try another.",
                                style="bold bright_black",
                                width=59,
                                title="[bold bright_black]> [Error] <",
                            )
                        )
                else:
                    printf(
                        Panel(
                            f"[bold red]File not found!",
                            style="bold bright_black",
                            width=59,
                            title="[bold bright_black]> [Error] <",
                        )
                    )
                sys.exit()
            elif CHOOSE in ["7", "07"]:
                printf(
                    Panel(
                        f"[bold white]Exiting... thank you for using this tool!",
                        style="bold bright_black",
                        width=59,
                        title="[bold bright_black]> [Exit] <",
                    )
                )
                sys.exit()
            else:
                printf(
                    Panel(
                        f"[bold red]Invalid option. Please try again.",
                        style="bold bright_black",
                        width=59,
                        title="[bold bright_black]> [Invalid Choice] <",
                    )
                )
                time.sleep(3)
                self.UTAMA()
        except Exception as e:
            printf(
                Panel(
                    f"[bold red]{str(e).capitalize()}!",
                    style="bold bright_black",
                    width=59,
                    title="[bold bright_black]> [Error] <",
                )
            )
            sys.exit()

    def TAMPILKAN_LOGO(self):
        os.system("cls" if os.name == "nt" else "clear")
        printf(
            Panel(
                r"""[bold red]    ______    _          __  __       _ _           
   |  ____|  | |        |  \/  |     (_) |          
   | |__ __ _| | _____  | \  / | __ _ _| | ___ _ __ 
   |  __/ _` | |/ / _ \ | |\/| |/ _` | | |/ _ \ '__|
   | | | (_| |   <  __/ | |  | | (_| | | |  __/ |   
   [bold white]|_|  \__,_|_|\_\___| |_|  |_|\__,_|_|_|\___|_|   
          [underline green]Fake Email Generator - by Rozhak""",
                style="bold bright_black",
                width=59,
            )
        )
        return False


class CHECKER:
    def EMAIL(self, email, file_live, file_die):
        global LIVE, DIE, UNKNOWN, LOOPING
        try:
            for EMAIL in email:
                if "@" in EMAIL and "." in EMAIL:
                    with requests.Session() as session:
                        session.headers.update({
                            "User-Agent": "Mozilla/5.0",
                        })
                        response = session.get(
                            "https://ychecker.com/app/payload?",
                            params={"email": EMAIL},
                        )
                        if '"items":' in response.text:
                            payload = json.loads(response.text)["items"]
                            session.headers.update({
                                "Origin": "https://ychecker.com"
                            })
                            response2 = session.get(
                                "https://app.sonjj.com/v1/check_email/?",
                                params={"payload": payload},
                            )
                            status = json.loads(response2.text).get("status", "")
                            if status == "Ok":
                                LIVE.append(EMAIL)
                                open(file_live, "a+").write(EMAIL + "\n")
                            elif status == "NotExist":
                                DIE.append(EMAIL)
                                open(file_die, "a+").write(EMAIL + "\n")
                            else:
                                UNKNOWN.append(EMAIL)
                LOOPING += 1
                printf(
                    f"[bold bright_black]   ──>[bold green] @{EMAIL.split('@')[0]}[bold white]/[bold blue]{LOOPING}[bold white] LIVE:-[bold green]{len(LIVE)}[bold white] DIE:-[bold red]{len(DIE)}[bold white] BAD:-[bold yellow]{len(UNKNOWN)}     ",
                    end="\r",
                )
        except Exception as e:
            printf(f"[bold red]Error: {str(e)}")
            time.sleep(5)


class EMAILS:
    def RANDOM_STRING(self, domain, count, file_name, length=10):
        for _ in range(int(count)):
            name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
            email = f"{name}{domain}"
            open(file_name, "a+").write(email + "\n")
            printf(
                f"[bold bright_black]   ──>[bold green] {email}[bold white]     ",
                end="\r",
            )
            time.sleep(0.005)
        return True

    def MIMESIS(self, domain, count, file_name):
        for _ in range(int(count)):
            email = Person(Locale.EN).email(domains=[domain])
            open(file_name, "a+").write(email + "\n")
            time.sleep(0.005)
        return True

    def FAKER(self, domain, count, file_name):
        faker = Faker()
        for _ in range(int(count)):
            email = faker.email(domain=domain.replace("@", ""))
            open(file_name, "a+").write(email + "\n")
            time.sleep(0.005)
        return True

    def NAMES(self, domain, count, file_name):
        for _ in range(int(count)):
            fname = names.get_first_name().lower()
            lname = names.get_last_name().lower()
            email = f"{fname}.{lname}{domain}"
            open(file_name, "a+").write(email + "\n")
            time.sleep(0.005)
        return True

    def RANDOM_USER(self, domain, count, file_name):
        for _ in range(int(count)):
            user = RandomUser()
            email = user.get_email().replace("@example.com", domain)
            open(file_name, "a+").write(email + "\n")
            time.sleep(0.005)
        return True

    def GENERATE_RANDOM_FILENAME(self, length=9, extension=".txt", folder="."):
        filename = f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=length))}{extension}"
        filepath = os.path.join(folder, filename)
        with open(filepath, "w") as f:
            f.write("")
        return filepath


if __name__ == "__main__":
    try:
        FITUR().UTAMA()
    except Exception as e:
        printf(Panel(f"[bold red]{str(e).capitalize()}!", style="bold bright_black", width=59, title="[bold bright_black]> [Error] <"))
        sys.exit()
    except KeyboardInterrupt:
        sys.exit()
