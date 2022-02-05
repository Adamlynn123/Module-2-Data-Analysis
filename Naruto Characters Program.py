import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Module 2, Data Analysis/Naruto Characters.csv")


def main():
    choice = int(input("What would you like to learn more about? \n\
    village(1)\n\
    ranking(2)\n\
    "))

    if choice == 1:
        filter_characters_by_village()
    elif choice == 2:
        sort_characters_by_rank()
    else: 
        print("Invalid choice, please try again.")


def filter_characters_by_village():
    
    village_choice = int(input("Choose a Village to see which characters are in it.\n\
        Leaf(1)\n\
        Sand(2)\n\
        Stone(3)\n\
        Rain(4)\n\
        Cloud(5)\n\
        Mist(6)\n\
        Hot Spring(7)\n\
        Sound(8)\n\
        \n\
        "))

    if village_choice == 1:
        filter_value = "Leaf"
    elif village_choice == 2:
        filter_value = "Sand"
    elif village_choice == 3:
        filter_value = "Stone"
    elif village_choice == 4:
        filter_value = "Rain"
    elif village_choice == 5:
        filter_value = "Cloud"
    elif village_choice == 6:
        filter_value = "Mist"
    elif village_choice == 7:
        filter_value = "Hot Spring"
    elif village_choice == 8:
        filter_value = "Sound"
    else:
        print("Invalid Choice")


    sort_type = int(input("How do you want to sort?\n\
        Age(1)\n\
        Ranking(2)\n\
        Alphabetical(3)\n\
        "))

    if sort_type == 1:
        sort_value = "Age"
    elif sort_type == 2:
        sort_value = "Ranking"
    elif sort_type == 3:
        sort_value = "Name"


    filtered_data_frame = (df.loc[df['Village'] == filter_value])
    sorted_data_frame = filtered_data_frame.sort_values(sort_value, ascending=False)

    print(sorted_data_frame)




def sort_characters_by_rank():
    rank_choice = int(input("Type what rank do you want to look into? (1-10) or (0) for all ranks: "))


    if rank_choice > 0 < 11:
        filtered_data_frame = (df.loc[df['Ranking'] == rank_choice])

        stats = filtered_data_frame.agg(
            {
                "Age": ["min", "max", "median", "mean", "std"],
            }
        )
        print(stats)

    elif rank_choice == 0:
        average_age_per_rank = df[["Ranking", "Age"]].groupby("Ranking").mean()
        average_age_per_rank.plot()
        print(average_age_per_rank)
        plt.show()
    
    else:
        print("Invalid Choice")
        
if __name__ == "__main__":
    main()