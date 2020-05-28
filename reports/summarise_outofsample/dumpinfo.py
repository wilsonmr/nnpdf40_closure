"""
abuse the datasets_properties_table from validphys to work with vp runcard

"""
import pathlib

from validphys.fitdata import datasets_properties_table

class Fakefit:
    def __init__(self, path: str):
        self.path = pathlib.Path(path)

def main():
    full = "./fullout"
    part = "./partial"
    df_full = datasets_properties_table(fit=Fakefit(full))

    with open("./summarise_fullout_data.tex", "w+") as f:
        df_full.to_latex(f, float_format="{:0.2f}".format,)

    df_part = datasets_properties_table(fit=Fakefit(part))
    with open("./summarise_partial_data.tex", "w+") as f:
        df_part.to_latex(f, float_format="{:0.2f}".format,)

if __name__ == "__main__":
    main()
