"""
Day 4 initial solution
Benjamin Wheeler
"""
import re


def part1() -> int:
    with open('day4.input', 'r') as f:
        passports = f.read().split('\n\n')  # Splits by blank line

    required: set = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    pattern = re.compile(r'[\n ]')

    valid_passports = 0

    for passport in passports:

        passport = re.split(pattern, passport)
        credentials: set = {e.split(':')[0] for e in passport}

        # Get the required elements that are missing from this passport.
        missing = required.difference(credentials)

        if len(missing) == 0 or missing == {'cid'}:
            valid_passports += 1

    return valid_passports


def part2() -> int:
    with open('day4.input', 'r') as f:
        passports = f.read().split('\n\n')  # Splits by blank line

    # Regex patterns and other checkers
    passport_pattern = re.compile(r'[\n ]')
    hcl_pattern = re.compile(r'^#[0-9a-f]{6}$')
    height_pattern = re.compile(r'^(\d+)(\D+)$')
    pid_pattern = re.compile(r'^\d{9}$')
    required_credentials = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    valid_passports = 0

    for passport in passports:
        passport = re.split(passport_pattern, passport)

        # Get credentials.
        creds = dict(e.split(':') for e in passport)

        # Check each required field exists.
        missing: set = required_credentials.difference(creds.keys())

        if len(missing) > 0 and 'cid' not in missing:
            continue  # To next passport

        #############################################################

        # Next, check each individual field.
        # Birth year
        if not 1920 <= int(creds['byr']) <= 2002:
            continue

        # Issue year
        if not 2010 <= int(creds['iyr']) <= 2020:
            continue

        # Expiration year
        if not 2020 <= int(creds['eyr']) <= 2030:
            continue

        # Height
        if temp := re.match(height_pattern, creds['hgt']):
            height, unit = temp.groups()
        else:
            continue

        if unit == 'cm' and not 150 <= int(height) <= 193:
            continue
        elif unit == 'in' and not 59 <= int(height) <= 76:
            continue

        # Hair color
        if not re.match(hcl_pattern, creds['hcl']):
            continue

        # Eye color
        if not creds['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            continue

        # Passport ID
        if not re.match(pid_pattern, creds['pid']):
            continue

        # Country id ignored
        valid_passports += 1

    return valid_passports


if __name__ == '__main__':
    print('Running day 4...')
    answer = part1()
    print(answer)

    answer = part2()
    print(answer)
    print('Done.')
