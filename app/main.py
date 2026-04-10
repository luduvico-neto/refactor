from core import lifespan


with lifespan() as fuzzy_checker:
    fuzzy_checker.compare_word()
