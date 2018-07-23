function ValidateNumber(e, pnumber)
{
    if (!/^\d+$/.test(pnumber))
    {
        e.value = /^\d+/.exec(e.value);
    }
    return false;
}