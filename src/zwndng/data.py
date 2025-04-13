import importlib.resources as resources


def sach_pdf_path():
    return resources.files("zwndng") / "data" / "sach.pdf"


def geld_pdf_path():
    return resources.files("zwndng") / "data" / "geld.pdf"


def sammel_pdf_path():
    return resources.files("zwndng") / "data" / "sammel.pdf"
