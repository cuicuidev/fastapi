import models
import datetime

now = round(datetime.datetime.now().timestamp())

fake_entry_table = [
    models.Entry(id=0, exercise_id=0, n_repetitions=6, weight_kg=100.0, performed = now),
    models.Entry(id=1, exercise_id=0, n_repetitions=6, weight_kg=100.0, performed = now + 300*1),
    models.Entry(id=2, exercise_id=0, n_repetitions=5, weight_kg=100.0, performed = now + 300*2),
    models.Entry(id=3, exercise_id=0, n_repetitions=4, weight_kg=100.0, performed = now + 300*3),
    models.Entry(id=4, exercise_id=1, n_repetitions=11, weight_kg=70.0, performed = now + 300*4),
    models.Entry(id=5, exercise_id=1, n_repetitions=10, weight_kg=70.0, performed = now + 300*5),
    models.Entry(id=6, exercise_id=1, n_repetitions=10, weight_kg=70.0, performed = now + 300*6),
    models.Entry(id=7, exercise_id=1, n_repetitions=8, weight_kg=70.0, performed = now + 300*7),
    models.Entry(id=8, exercise_id=2, n_repetitions=14, weight_kg=30.0, performed = now + 300*8),
    models.Entry(id=9, exercise_id=2, n_repetitions=13, weight_kg=30.0, performed = now + 300*9),
    models.Entry(id=10, exercise_id=2, n_repetitions=13, weight_kg=30.0, performed = now + 300*10),
    models.Entry(id=11, exercise_id=3, n_repetitions=13, weight_kg=14.0, performed = now + 300*11),
    models.Entry(id=12, exercise_id=3, n_repetitions=11, weight_kg=14.0, performed = now + 300*12),
    models.Entry(id=13, exercise_id=4, n_repetitions=12, weight_kg=16.0, performed = now + 300*13),
    models.Entry(id=14, exercise_id=4, n_repetitions=9, weight_kg=16.0, performed = now + 300*14),
]

fake_exercise_table = [
    models.Exercise(id=0, name="back_squat"),
    models.Exercise(id=1, name="bench_press"),
    models.Exercise(id=2, name="unilateral_row"),
    models.Exercise(id=3, name="tricep_pulldown"),
    models.Exercise(id=4, name="bicep_curl")
]

fake_db = {
    "entries" : fake_entry_table,
    "exercises" : fake_exercise_table,
}