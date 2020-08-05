def response(hey_bob):
    yelling = hey_bob.isupper()
    bob = hey_bob.rstrip()
    if len(bob) == 0:
        return "Fine. Be that way!"
    else:
        if bob[-1]=="?":
            if yelling:
                return "Calm down, I know what I'm doing!"
            else:
                return "Sure."
        else:
            if yelling:
                return "Whoa, chill out!"
            else:
                return "Whatever."
