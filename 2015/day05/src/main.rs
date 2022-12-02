
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
    todo!();
}

fn main() {
    let contents = include_str!("../day05_input.txt").to_string();

    let mut num_nice = 0;
    for l in contents.lines() {
        if is_nice1(l.to_string()) {
            num_nice += 1;
        }
    }

    println!("Part 1: {num_nice}");
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

#[test]
fn example6() {
    let contents = String::from("qjhvhtzxzqqjkmpb");
    assert!(is_nice2(contents));
}
