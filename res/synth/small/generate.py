from incal.generator import generate_formula_file, generate_data_files, clean_dir
import os


clean_dir(os.path.dirname(__file__))

for i in range(10):
    f = generate_formula_file(
        os.path.dirname(__file__),
        "small",
        2,
        2,
        "cnf",
        2,
        2,
        2,
        1000,
        30,
        suffix=str(i),
    )

    for j in range(10):
        generate_data_files(f, sample_count=1000, suffix=str(j))