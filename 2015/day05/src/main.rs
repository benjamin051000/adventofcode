use std::collections::HashSet;

fn is_nice1(word: String) -> bool {
    let mut num_vowels = 0;
    let mut double_letter = false;

    for c in word.chars() {
        // 1. Check for at least 3 vowels
        match c {
            'a'  | 'e' | 'i' | 'o' | 'u' => num_vowels += 1,
            _ => () // Do nothing
        }
    }

    for pair in word.as_bytes().windows(2) {

        // Destructure into two variables
        let [first, second] = match pair {
            &[f, s] => [f, s],
            _ => unreachable!()
        };

        if first == second {
            double_letter = true;
        }

        // 3. Ensure it does not contain the following
        // ab, cd, pq, xy
        match pair {
            b"ab" | b"cd" | b"pq" | b"xy" => return false,
            _ => ()
        }
    }
    
    num_vowels >= 3 && double_letter
}

fn is_nice2(word: String) -> bool {
    let mut double_pair = false;
    let mut seen: HashSet<[u8; 2]> = HashSet::new();

    // Find non-overlapping pairs of 2 chars
    // Stepping by 2 ensures no overlap!
    for pair in word.as_bytes().chunks(2) {
        let pair: [u8; 2] = pair.try_into().unwrap(); // BUG Panicks for odd-length words

        // Have we seen this before?
        if seen.contains(&pair) {
            double_pair = true;
            break;
        }
        // Add to visited
        seen.insert(pair);
    }

    // Find xyx, where x is any letter, and y is any different letter.
    let mut xyx = false;
    for pair in word.as_bytes().windows(3) {
        let [a, b, c]: [u8; 3] = pair.try_into().unwrap();
        if a == c && a != b {
            xyx = true;
            break;
        }

    }

    xyx && double_pair
}

fn part1(input: &String) -> i32 {
    let mut num_nice = 0;

    for l in input.lines() {
        if is_nice1(l.to_string()) {
            num_nice += 1;
        }
    }
    num_nice
}

fn part2(input: &String) -> i32 {
    let mut num_nice = 0;
    for l in input.lines() {
        if is_nice2(l.to_string()) {
            num_nice += 1;
        }
    }

    num_nice
}

fn main() {
    let contents = include_str!("../day05_input.txt").to_string();
    println!("Part 1: {}", part1(&contents));
    println!("Part 2: {}", part2(&contents));
}


#[test]
fn example1() {
    let contents = "ugknbfddgicrmopn".to_string();
    assert!(is_nice1(contents));
}

#[test]
fn example2() {
    let contents = String::from("aaa");
    assert!(is_nice1(contents));
}

#[test]
fn example3() {
    let contents = String::from("jchzalrnumimnmhp");
    assert!(!is_nice1(contents));
}

#[test]
fn example4() {
    let contents = String::from("haegwjzuvuyypxyu");
    assert!(!is_nice1(contents));
}


#[test]
fn example5() {
    let contents = String::from("dvszwmarrgswjxmb");
    assert!(!is_nice1(contents));
}

// Part 2 tests

#[test]
fn example6() {
    let contents = String::from("qjhvhtzxzqqjkmpb");
    assert!(is_nice2(contents));
}

#[test]
fn example7() {
    let contents = String::from("xxyxx");
    assert!(is_nice2(contents));
}

#[test]
fn example8() {
    let contents = String::from("uurcxstgmygtbstg");
    assert!(!is_nice2(contents));
}

#[test]
fn example9() {
    let contents = String::from("ieodomkazucvgmuy");
    assert!(!is_nice2(contents));
}
