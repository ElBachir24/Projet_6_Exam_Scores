# =====================================================================
# PROJECT 6: EXAM SCORES OF A CLASS
#
# TEAM MEMBERS:
# - Group leader / Member 5 : Diouf Mouhamed El Bachir
# - Member 1: Ousseynou Sow
# - Member 2: MINGANE GRACIA
# - Member 3: Dlamini Sandziso Siyabonga
# - Member 4: Nusaiba Alrasheed Osman Alfaki
# =====================================================================

# Datasets provided in the assignment
class_a = [56, 62, 71, 48, 65, 59, 73, 66, 62, 68, 61, 45, 77, 64, 58, 69, 63, 62, 95, 60]

class_b = [58, 60, 61, 59, 62, 57, 63, 60, 61, 59, 60, 62, 58, 61, 60, 59, 62, 60, 61, 60]


# --- TASK 1: Member 1 (Ousseynou Sow) - mean & median ---
def mean(data):
    """Calculates the arithmetic average of a list of numbers."""
    return sum(data) / len(data)


def median(data):
    """Calculates the middle value of a sorted list of numbers."""
    s_data = sorted(data)
    n = len(s_data)
    mid = n // 2
    if n % 2 != 0:
        return s_data[mid]
    else:
        return (s_data[mid - 1] + s_data[mid]) / 2


# --- TASK 2: Member 2 (MINGANE GRACIA) - mode & std_dev ---
def mode(data):
    """Finds the most frequent score using a frequency dictionary."""
    appears = {}
    for x in data:
        appears[x] = appears.get(x, 0) + 1

    max_count = 0
    mod = data
    for key, value in appears.items():
        if value > max_count:
            max_count = value
            mod = key
    return mod


def std_dev(data):
    """Calculates standard deviation without external libraries."""
    m = mean(data)
    sum_squares = 0
    for x in data:
        sum_squares += (x - m) ** 2
    variance = sum_squares / len(data)
    return variance ** 0.5


# --- TASK 3: Member 3 (Dlamini Sandziso Siyabonga) - outliers ---
def outliers(data):
    """Returns a list of scores deviating from mean by more than 2 std dev."""
    m = mean(data)
    sigma = std_dev(data)
    outlier_list = []
    for score in data:
        if abs(score - m) > 2 * sigma:
            outlier_list.append(score)
    return outlier_list


# --- EXTRA / BONUS: Member 4 (Nusaiba Alrasheed Osman Alfaki) - grade_histogram ---
def grade_histogram(data):
    """Displays a grade breakdown histogram using stars."""
    groups = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    for score in data:
        if score >= 70:
            groups['A'] += 1
        elif score >= 60:
            groups['B'] += 1
        elif score >= 50:
            groups['C'] += 1
        else:
            groups['D'] += 1

    for group, count in groups.items():
        print(f"{group}: {'*' * count}")


# --- TASK 4 & MAIN: Leader / Member 5 (Diouf Mouhamed El Bachir) ---
def main():
    print("==========================================")
    print("      PROJECT 6: CLASS EXAM STATS         ")
    print("==========================================\n")

    # --- CLASS A ANALYSIS ---
    print("--- CLASS A STATS ---")
    print(f"Mean (with outlier)   : {mean(class_a):.2f}")
    print(f"Median (with outlier) : {median(class_a):.2f}")
    print(f"Mode                  : {mode(class_a)}")
    print(f"Std Dev               : {std_dev(class_a):.2f}")
    
    out_a = outliers(class_a)
    print(f"Outliers detected     : {out_a}")

    # Remove outliers for comparison
    clean_a = [x for x in class_a if x not in out_a]
    print(f"\nMean (WITHOUT outlier)   : {mean(clean_a):.2f}")
    print(f"Median (WITHOUT outlier) : {median(clean_a):.2f}")

    # --- CLASS B ANALYSIS ---
    print("\n--- CLASS B STATS ---")
    print(f"Mean     : {mean(class_b):.2f}")
    print(f"Median   : {median(class_b):.2f}")
    print(f"Mode     : {mode(class_b)}")
    print(f"Std Dev  : {std_dev(class_b):.2f}")
    print(f"Outliers : {outliers(class_b)}")

    # --- COMPARISON ---
    print("\n--- COMPARISON SUMMARY ---")
    if mean(class_a) > mean(class_b):
        print("- Class A has a higher average score than Class B.")
    else:
        print("- Class B has a higher average score than Class A.")

    if std_dev(class_a) > std_dev(class_b):
        print("- Class A has a much higher standard deviation (more spread out).")
    else:
        print("- Class B has a higher standard deviation.")

    # --- HISTOGRAMS ---
    print("\n--- Grade Distribution: Class A ---")
    grade_histogram(class_a)

    print("\n--- Grade Distribution: Class B ---")
    grade_histogram(class_b)




if __name__ == "__main__":
    main()
