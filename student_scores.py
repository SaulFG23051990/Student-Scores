def analyze_scores(scores: list[list[int]]) -> None:
    """
    Input: It takes a list
    Process: it evaluates the numbers in it
    Output: It gives back the results based off the numbers
    """
    average_scores = []
    over_90 = 0
    high_score = 0
    
    # Calculate averages
    for i in range(len(scores)):
        average = sum(scores[i]) / len(scores[i])
        average_scores.append(average)
            
    print("All Scores:")
    for i in range(len(scores)):
        # Fixed: Format scores cleanly without Python list brackets []
        

        print(f"Student {i+1}:", end= " ")
        for j in range(len(scores[i])):
            print(scores[i][j],end= " ")
        print()
    print("Averages:")
    for i in range(len(scores)):
        print(f"Student {i+1} average: {round(average_scores[i],2)}")
        
    # Fixed: Count individual scores that are >= 90 across the entire grid
    for i in range(len(scores)):
        for score in scores[i]:
            if score >= 90:
                over_90 += 1
    print(f"Scores >= 90: {over_90}")
    
    # Find highest score
    for i in range(len(scores)):
        for j in range(len(scores[i])):
            if high_score < scores[i][j]:
                high_score = scores[i][j]
    print(f"Highest score: {high_score}")


def main():
    scores = [
        [80, 90,  85],
        [70, 88,  92],
        [95, 100, 98],
        [60, 75,  70]
    ]
    analyze_scores(scores)


if __name__ == "__main__":
    main()
