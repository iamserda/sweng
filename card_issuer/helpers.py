import random

amex_issued_set = set()
visa_issued_set = set()
master_issued_set = set()


def issue_card(user_credit):
    """issue card based on credit"""
    if user_credit < 300 or user_credit > 850:
        print("One of our Client Concierge will be with your shorty!")
        return None

    if user_credit >= 720:
        print("Excellent, we can offer you the Deluxe AMEX card.\nProcessing....\n")
        return select_card("amex")

    if user_credit >= 690:
        print("Great, we can offer you our Premium VISA card.\nProcessing....\n")
        return select_card("visa")

    if user_credit >= 630:
        print(
            "Awesome, we can offer you own of our Premium MASTERCard.\nProcessing....\n"
        )
        return select_card("master")


def get_servicers():
    """returns an object of card servicers available at the firm"""
    return {
        "amex": {"function": amex_factory, "issued": amex_issued_set},
        "visa": {"function": visa_factory, "issued": visa_issued_set},
        "master": {"function": master_factory, "issued": master_issued_set},
    }


def select_card(pmt_servicer: str) -> str:
    """selects card for customer"""
    if not pmt_servicer or pmt_servicer not in ["amex", "visa", "master"]:
        error_message = "Card Payment Servicer was not provided. Info logged. Application   will terminate now."
        raise ValueError(error_message)
    servicers = get_servicers()
    card_generator = servicers[pmt_servicer]["function"]
    issued_cards_set = servicers[pmt_servicer]["issued"]
    return generate_card(pmt_servicer, card_generator, issued_cards_set)


def generate_card(svc, card_generator, verifier):
    """generates a new card based on servicer:str, card_generator:def, verifier:set"""
    new_card = card_generator()
    while new_card in verifier:
        new_card = card_generator()
    return new_card


def amex_factory():
    """generates a fake amex card"""
    amex_id = random.randint(32000, 85000)
    group_nums = random.randint(312123, 985430)
    customer_nums = random.randint(32000, 85000)
    return f"{amex_id}-{group_nums}-{customer_nums}"


def visa_factory():
    """generates a fake visa card"""
    visa_id = random.randint(4100, 4999)
    bank_id = random.randint(1111, 9000)
    group_id = random.randint(1110, 9900)
    client_id = random.randint(1100, 9990)
    return f"{visa_id}-{bank_id}-{group_id}-{client_id}"


def master_factory():
    """a fake master card generator"""

    issuer_id = random.randint(5100, 5999)
    group_id1 = random.randint(1111, 9999)
    group_id2 = random.randint(1111, 9999)
    customer_id = random.randint(1111, 9999)
    return f"{issuer_id}-{group_id1}-{group_id2}-{customer_id}"
