from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

while True:

    print("\n\033[1mHi there! Welcome to my program, a Student Performance analysis for class teachers!!\033[0m\n" \
          "\n\033[1mPLEASE GO THROUGH BELOW OPTIONS AND CHOOSE ONE OF THE FOLLOWING\033[0m\n")

    mode = input("\n1. A graph showing the distribution of the total marks among students in your class \n" \
                 "\n2. A chart to show each subject's share in the total marks for a student in your class \n" \
                 "\n3. A chart showing the trend of the total marks of a student over multiple terms\n" \
                 "\n4. Use the EXCEL file to see the distribution of the total marks of students updated\n" \
                 "\n\033[1mNOTE : IF YOU ARE USING THE EXCEL FILE," \
                 " PLEASE NOTE ANY ROWS WITH NULL VALUES WILL NOT BE USED IN THE CHART TO ENSURE ACCURACY \n" \
                 "\n\nPlease choose \033[1m1, 2, 3, 4\033[0m or type \033[1mq\033[0m to Quit :\033[0m ").lower()

    if mode == 'q':
        break

    elif mode == '1':
        while True:
            try:
                total = int(input('\nEnter Total Number of Students: '))
            except ValueError:
                print("\n⚠️ Please enter a valid number for total students!\n\n\n")
                continue

            stu = []
            mrks = []

            print('\n\033[1mPLEASE ENTER EACH STUDENT NAME AND THEIR MARKS ONE BY ONE\033[0m\n')

            for i in range(total):
                e_stu = input('\nEnter the Student Name : ').upper()
                stu.append(e_stu)
                try:
                    s_mrk = int(input("Enter their Total Marks : "))
                except ValueError:
                    print("\n⚠️ Invalid input detected.\n Restarting student entry to keep the data accurate.\n")
                    break
                mrks.append(s_mrk)

            else:

                df = pd.DataFrame({'Student Name': stu, 'Marks': mrks})

                df.drop_duplicates(inplace=True)

                sns.barplot(x='Student Name', y='Marks', data=df, color='black', width=.4, edgecolor='y',
                            label='Marks scored')
                plt.title('MARKS SCORED BY EACH STUDENT')
                plt.xlabel('Student')
                plt.ylabel('Marks earned')
                plt.legend()
                plt.ylim(0, 600)
                plt.show()
                break

    elif mode == '2':
        while True:
            stu_name = str(input('\nEnter Student Name: ')).upper()
            try:
                no_sub = int(input('\nPlease Enter the number of Subjects for the Student: '))
            except ValueError:
                print("\n⚠️ Please enter a valid number for total subjects!\n\n\n")
                continue

            subj = []
            mrk = []
            expd = []
            exp = 0

            print('\n\033[1mPLEASE ENTER EACH SUBJECT AND ITS MARKS ONE BY ONE\033[0m\n')

            for i in range(no_sub):
                e_sub = input('\nEnter the Subject Name : ').upper()
                subj.append(e_sub)
                try:
                    e_mrk = int(input("Enter Marks for the Subject: "))
                except ValueError:
                    print("\n⚠️ Invalid input detected.\n Restarting subject entry to keep the data accurate.\n")
                    break
                mrk.append(e_mrk)
            else:

                for i in subj:
                    exp += .02
                    expd.append(exp)

                plt.pie(mrk, labels=subj, explode=expd, shadow=True, autopct='%1.1f%%')
                plt.title(f'SHARE OF TOTAL MARKS PER SUBJECT FOR {stu_name}')
                plt.show()
                break

    elif mode == '3':
        while True:
            st_name = input('\nEnter the Name of the Student: ').upper()
            try:
                no_tms = int(input('\nEnter Total number of Terms you wish to analyze marks for: '))
            except ValueError:
                print("\n⚠️ Please enter a valid number for total terms!\n\n\n")
                continue
            tms = []
            mks = []

            print('\n\033[1mPLEASE ENTER EACH TERM AND RESPECTIVE MARKS ONE BY ONE\033[0m\n')

            for i in range(no_tms):
                e_tm = input('\nEnter Term Name/No. : ').upper()
                tms.append(e_tm)
                try:
                    e_mks = int(input('Enter Marks for the Term : '))
                except ValueError:
                    print("\n⚠️ Invalid input detected.\n Restarting subject entry to keep the data accurate.\n")
                    break
                mks.append(e_mks)
            else:

                df = pd.DataFrame({'Terms': tms, 'Marks': mks})

                df.drop_duplicates(inplace=True)

                sns.lineplot(x='Terms', y="Marks", linestyle='--', data=df, marker='o', markerfacecolor='#BA8E23',
                             markersize=10, color='black', linewidth=4, label='Marks earned')
                plt.title(f'MARKS TREND OVER TERMS FOR {st_name}')
                plt.xlabel('Terms')
                plt.ylabel('Marks scored')
                plt.grid(axis='both', linestyle='--', color='#D3D3D3', linewidth=2)
                plt.show()

                break

    elif mode == '4':

        df = pd.read_excel(r'C:\Users\HP\OneDrive\Documents\PYTHON\Project_program\Marklist.xlsx')
        opt = input('\n\033[1mYou have chosen to use the excel file, Please Choose one of the below options\033[0m\n' \
                    ' \n1.Chart showing Marks by Student Name \n' \
                    '\n2.Chart showing Marks by Student Roll Number \n' \
                    '\nPlease choose \033[1m1, 2\033[0m or type \033[1mb\033[0m to go to Main Menu: ').lower()
        if opt == 'b':
            print('\n\nGoing Back to Main Menu....')
            continue

        elif opt == '1':

            df = df[['Name', 'Marks']]

            df.dropna(inplace=True)

            df.drop_duplicates(inplace=True)

            sns.barplot(x='Name', y='Marks', data=df, color='black', edgecolor='y', width=.5, label='Marks')
            plt.title('MARKS BY EACH STUDENT')
            plt.ylim(0, 600)
            plt.legend()
            plt.show()
            break

        elif opt == '2':

            df = df[['RollNo', 'Marks']]

            df.dropna(inplace=True)

            df.drop_duplicates(inplace=True)

            sns.barplot(x='RollNo', y='Marks', data=df, color='black', edgecolor='y', width=.5, label='Marks')
            plt.title('MARKS BY EACH STUDENT')
            plt.ylim(0, 600)
            plt.legend()
            plt.show()
            break

        else:
            print("\n\n⚠️ Invalid option! Going back to Main Menu..")
            continue


    else:
        print('\nInvalid option, please choose a valid option!\n\n')

print('\nExit Success!Thank you for using my program! 😊 \n\n\n')