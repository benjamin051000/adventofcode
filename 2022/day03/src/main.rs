use std::collections::HashSet;
#[cfg(test)]
use std::collections::HashMap;


fn split_in_half(line: &str) -> [&str; 2] {
    let halfway = line.len() / 2;

    let left = &line[..halfway];
    let right = &line[halfway..];

    assert_eq!(left.len(), right.len());

    [left, right]
}


fn get_common<'a>(l_letters: &'a str, r_letters: &'a str) -> char {
    let mut l_rucksack: HashSet<char> = HashSet::new();
    let mut r_rucksack: HashSet<char> = HashSet::new();

    for c in l_letters.chars() {
        l_rucksack.insert(c);
    }
    for c in r_letters.chars() {
        r_rucksack.insert(c);
    }

    let s: HashSet<_> = l_rucksack.intersection(&r_rucksack).collect();
    if let Some(c) = s.iter().next().cloned() {
        *c
    }
    else {
        unreachable!();
    }
}

fn get_three<'a>(a: &'a str, b: &'a str, c: &'a str) -> char {
    let x: HashSet<_> = a.chars().collect();
    let y: HashSet<_> = b.chars().collect();
    let z: HashSet<_> = c.chars().collect();

    let first_two = x.intersection(&y).copied().collect::<HashSet<char>>();

    let all_three = first_two.intersection(&z).collect::<HashSet<_>>();

    if let Some(c) = all_three.iter().next().cloned() {
        *c
    }
    else {
        unreachable!();
    }
}


fn get_priority(c: char) -> u32 {
    if c.is_uppercase() {
        c as u32 - 'A' as u32 + 27
    }
    else {
        c as u32 - 'a' as u32 + 1
    }
}



fn part1(contents: &String) -> u32 {
    let mut total = 0;
    for line in contents.lines() {
        let [l_half, r_half] = split_in_half(line);
        let common = get_common(l_half, r_half);
        total += get_priority(common);

    }

    total
}


fn part2(contents: &String) -> u32 {
    let mut total = 0;

    // Separate lines into groups of 3
    let mut v = [String::new(), String::new(), String::new()];

    let mut i = 0;
    for line in contents.lines() {
        if i >= 3 { i = 0; } // Clamp i from 0-2

        v[i] = String::from(line);

        // Every third go around...
        if i == 2 {
            assert_eq!(v.len(), 3);

            let [a, b, c] = &v;

            let common = get_three(a, b, c);

            total += get_priority(common);
        }

        i += 1;
    }

    total 
}


fn main() {
    let contents = std::fs::read_to_string("day03_input.txt").expect("Read file successfully");

    println!("Part 1: {}", part1(&contents));
    println!("Part 2: {}", part2(&contents));
}


#[test]
fn test_split_in_half() {

    let test = HashMap::from([
        ("vJrwpWtwJgWrhcsFMMfFFhFp", ["vJrwpWtwJgWr", "hcsFMMfFFhFp"]),
        ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", ["jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"]),
        ("PmmdzqPrVvPwwTWBwg", ["PmmdzqPrV", "vPwwTWBwg"])
    ]);

    for (original, [correct_l, correct_r]) in test {
        let [l, r] = split_in_half(original);
        assert_eq!(l, correct_l);
        assert_eq!(r, correct_r);
    }
}


#[test]
fn test_intersection() {
    let tests = HashMap::from([
        (["vJrwpWtwJgWr", "hcsFMMfFFhFp"], 'p'),
        (["jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"], 'L'),
        (["PmmdzqPrV", "vPwwTWBwg"], 'P')
    ]);

    for ([l, r], correct) in tests {
        assert_eq!(get_common(l, r), correct);
    }
}


#[test]
fn test_get_priority() {
    let tests = HashMap::from([
        ('a', 1),
        ('b', 2),
        ('z', 26),
        ('A', 27),
        ('B', 28),
        ('Z', 52)
    ]);

    for (c, p) in tests {
        assert_eq!(get_priority(c), p);
    }
}

#[test]
fn test_example1() {

    let contents = "vJrwpWtwJgWrhcsFMMfFFhFp\n\
                    jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n\
                    PmmdzqPrVvPwwTWBwg\n\
                    wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n\
                    ttgJtRGJQctTZtZT\n\
                    CrZsJsPPZsGzwwsLwLmpwMDw";

    assert_eq!(part1(&String::from(contents)), 157);
}


#[test]
fn test_example2() {

    let contents = "vJrwpWtwJgWrhcsFMMfFFhFp\n\
                    jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n\
                    PmmdzqPrVvPwwTWBwg\n\
                    wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n\
                    ttgJtRGJQctTZtZT\n\
                    CrZsJsPPZsGzwwsLwLmpwMDw";

    assert_eq!(part2(&String::from(contents)), 70);
}
