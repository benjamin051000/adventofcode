use std::collections::HashSet;
#[cfg(test)]
use std::collections::HashMap;

fn main() {
    let contents = std::fs::read_to_string("day03_input.txt").expect("Read file successfully");

    println!("Part 1: {}", part1(contents));
}

fn split_in_half(line: &str) -> [&str; 2] {
    let halfway = line.len() / 2;

    let left = &line[..halfway];
    let right = &line[halfway..];

    assert_eq!(left.len(), right.len());

    [left, right]
}

fn part1(contents: String) -> i32 {
    let mut l_rucksack: HashSet<char> = HashSet::new();
    let mut r_rucksack: HashSet<char> = HashSet::new();

    for line in contents.lines() {
        // Get both halves
        let [left_stuff, right_stuff] = split_in_half(line);


        for c in left_stuff.chars() {
            if !l_rucksack.insert(c) {

            }
        }

        for c in right_stuff.chars() {
            if !r_rucksack.insert(c) {

            }
        }

        let common: HashSet<_> = l_rucksack.intersection(&r_rucksack).collect();
        dbg!(common);
    }
    0
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
        (["vJrwpWtwJgWr", "hcsFMMfFFhFp"], "p"),
        (["jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"], "L"),
        (["PmmdzqPrV", "vPwwTWBwg"], "P")
    ]);
}

// let contents = "vJrwpWtwJgWrhcsFMMfFFhFp\n\
//                 jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n\
//                 PmmdzqPrVvPwwTWBwg\n\
//                 wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n\
//                 ttgJtRGJQctTZtZT\n\
//                 CrZsJsPPZsGzwwsLwLmpwMDw";
//
