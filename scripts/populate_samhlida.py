import os
from icealign import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'icealign.settings')
import codecs
import django

django.setup()

from samhlida.models import Corpus, Entry


def add_corpus(name):
    c = Corpus.objects.get_or_create(name=name)[0]
    c.save()
    return c


def add_entry(corpus,n, other_text, isl_text):
    e = Entry.objects.get_or_create(corpus=corpus, number=n, other_text=other_text, isl_text=isl_text)[0]
    e.save()
    return e


def populate():
    print('Populating Samhlida database!')

    file_dict = {
        "Biblían": ["biblian.txt"],
        "Fréttatilkynningar ESO": ["eso.txt"],
        "Hagstofa Íslands": ["hagstofan.txt"],
        "Íslendingasögur": ["fornritin.txt"],
        "KDE4": ["kde4.txt"],
        "Lyfseðlar EMA": ["ema00.txt", "ema01.txt", "ema02.txt", "ema03.txt", "ema04.txt", "ema05.txt", "ema06.txt", "ema07.txt", "ema08.txt"],
        "OpenSubtitles": ["opensubtitles00.txt", "opensubtitles01.txt", "opensubtitles02.txt", "opensubtitles03.txt", "opensubtitles04.txt", "opensubtitles05.txt", "opensubtitles06.txt", "opensubtitles07.txt", "opensubtitles08.txt", "opensubtitles09.txt", "opensubtitles10.txt", "opensubtitles11.txt", "opensubtitles12.txt", "opensubtitles13.txt", "opensubtitles14.txt", "opensubtitles15.txt", "opensubtitles16.txt", "opensubtitles17.txt", "opensubtitles18.txt", "opensubtitles19.txt", "opensubtitles20.txt", "opensubtitles21.txt", "opensubtitles22.txt", "opensubtitles23.txt", "opensubtitles24.txt", "opensubtitles25.txt"],
        "Skjöl EES": ["ees00.txt", "ees01.txt", "ees02.txt", "ees03.txt", "ees04.txt", "ees05.txt", "ees06.txt", "ees07.txt", "ees08.txt", "ees09.txt", "ees10.txt", "ees11.txt", "ees12.txt", "ees13.txt", "ees14.txt", "ees15.txt", "ees16.txt", "ees17.txt", "ees18.txt", "ees19.txt", "ees20.txt", "ees21.txt", "ees22.txt", "ees23.txt", "ees24.txt", "ees25.txt", "ees26.txt", "ees27.txt", "ees28.txt", "ees29.txt", "ees30.txt", "ees31.txt", "ees32.txt", "ees33.txt", "ees34.txt"],
        "Tatoeba": ["tatoeba.txt"],
        "Ubuntu": ["ubuntu.txt"],
        "Þýdd skáldverk": ["baekur.txt"],
    }

    entries = []
    for corpus_name, file_names in file_dict.items():
        corpus = add_corpus(corpus_name)
        for file_name in file_names:

            with codecs.open(os.path.join(settings.PARICE_DIR, file_name), "r", encoding="utf-8", errors='ignore') as f:
                for i, line in enumerate(f):
                    if not line or line == "\n":
                        continue
                    try:
                        other_text, isl_text = line.split('\t')
                    except:
                        continue

                    entries.append(Entry(corpus=corpus, number=i, other_text=other_text.strip(), isl_text=isl_text.strip()))
                    # e = add_entry(corpus=corpus, n=i, other_text=other_text.strip(), isl_text=isl_text.strip())
                    if len(entries) == 5000:
                        Entry.objects.bulk_create(entries)
                        entries = []
    if len(entries):
        Entry.objects.bulk_create(entries)

if __name__ == "__main__":
    populate()
