import math

def fv_basic(pv, rate, n):
    """
    Future value of a single lump sum.
    FV = PV * (1 + r)^n
    """
    return pv * (1 + rate) ** n


def pv_basic(fv, rate, n):
    """
    Present value of a single lump sum.
    PV = FV / (1 + r)^n
    """
    return fv / ((1 + rate) ** n)


def nper_basic(pv, fv, rate):
    """
    Number of periods for a single lump sum to grow from PV to FV.
    n = ln(FV/PV) / ln(1 + r)
    """
    if pv <= 0 or fv <= 0:
        raise ValueError("pv and fv must be > 0 for nper_basic.")
    if rate <= -1:
        raise ValueError("rate must be > -1 for nper_basic.")
    return math.log(fv / pv) / math.log(1 + rate)


def rate_basic(pv, fv, n):
    """
    Periodic rate for a single lump sum.
    r = (FV/PV)^(1/n) - 1
    """
    if pv <= 0 or fv <= 0:
        raise ValueError("pv and fv must be > 0 for rate_basic.")
    if n == 0:
        raise ValueError("n must be non-zero for rate_basic.")
    return (fv / pv) ** (1 / n) - 1

def fv(rate, nper, pmt=0, pv=0, when='end'):
    """
    Future Value of an investment or loan.
    """
    when_factor = 1 if when == 'begin' else 0
    return pv * (1 + rate) ** nper + pmt * ((1 + rate) ** nper - 1) / rate * (1 + rate) ** when_factor


def pv(rate, nper, pmt=0, fv=0, when='end'):
    """
    Present Value of an investment or loan.
    """
    when_factor = 1 if when == 'begin' else 0
    return (fv + pmt * (1 + rate * when_factor) * ((1 + rate) ** nper - 1) / rate) / (1 + rate) ** nper


def pmt(rate, nper, pv=0, fv=0, when='end'):
    """
    Payment required per period.
    """
    when_factor = 1 if when == 'begin' else 0
    return (-(fv + pv * (1 + rate) ** nper) * rate) / ((1 + rate * when_factor) * ((1 + rate) ** nper - 1))


def nper(rate, pmt=0, pv=0, fv=0, when='end'):
    """
    Number of periods required.
    """
    from math import log
    when_factor = 1 if when == 'begin' else 0
    return (log((pmt * (1 + rate * when_factor) - fv * rate) /
                (pmt * (1 + rate * when_factor) + pv * rate))
           ) / log(1 + rate)