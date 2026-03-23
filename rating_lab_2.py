import threading
import time
import random

global_rating = []

rating_lock = threading.Lock()

def process_subgroup(subgroup_name, students_data):
    print(f"Потік [{subgroup_name}] розпочав роботу...")
    
    for student_name, score in students_data.items():
        time.sleep(random.uniform(0.1, 0.3))
    
        with rating_lock:
            found = False
            for record in global_rating:
                if record['name'] == student_name:
                    record['score'] += score
                    found = True
                    break
            
            if not found:
                global_rating.append({'name': student_name, 'score': score})
                
            print(f"[{subgroup_name}] Додано {score} балів студенту {student_name}")

def main():
    subgroup1 = {"Іваненко": 15, "Петренко": 10, "Сидоренко": 20}
    subgroup2 = {"Іваненко": 5, "Коваленко": 25, "Сидоренко": 12}
    subgroup3 = {"Петренко": 8, "Коваленко": 10, "Мельник": 30}

    t1 = threading.Thread(target=process_subgroup, args=("Підгрупа 1", subgroup1))
    t2 = threading.Thread(target=process_subgroup, args=("Підгрупа 2", subgroup2))
    t3 = threading.Thread(target=process_subgroup, args=("Підгрупа 3", subgroup3))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Усі потоки завершили роботу.")
    
    print("Рейтинг Студентів")
    sorted_rating = sorted(global_rating, key=lambda x: x['score'], reverse=True)
    for index, student in enumerate(sorted_rating, start=1):
        print(f"{index}. {student['name']} — {student['score']} балів")

if __name__ == "__main__":
    main()
