try:
    f = open('mójplik.txt')
    s = f.readline()
    i = int(string.strip(s))
except IOError, (errno, strerror):
    print "Błąd I/O (%s): %s" % (errno, strerror)
except ValueError:
    print "Nie mogę przekształcić danej w liczbę całkowitą."
except:
    print "Nieobsługiwany błąd:", sys.exc_info()[0]
    raise
