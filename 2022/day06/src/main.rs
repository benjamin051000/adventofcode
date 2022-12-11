fn all_unique(elements: &[char]) -> bool {
    let mut h = std::collections::HashSet::new();
    for e in elements {
        if !h.insert(e) {
            return false;
        }
    }

    true
}

/// Finds first marker in a "stream" of chars.
fn first_marker(stream: &str) -> u32 {
    for (idx, fours) in stream.chars().collect::<Vec<char>>().windows(4).enumerate() {
        // Check if each of the fours are unique
        // if they are all different, then a != b && b != c && c != d
        dbg!(fours);
        if  all_unique(fours) {
            println!("They're all unique!");
            return idx as u32 + 4; // idx of first marker char + 4 = idx of ending marker char
        }

        println!("Some are equal.");
    }

    unreachable!();
}

fn part1(contents: &String) -> u32 {
    first_marker(contents)
}

fn part2(contents: &String) -> i32 {
    0
}

fn main() {
    let contents = std::fs::read_to_string("day06_input.txt").expect("Read file successfully");
    println!("Part 1: {}", part1(&contents));
    println!("Part 2: {}", part2(&contents));
}

#[test]
fn example1() {
    let contents = "mjqjpqmgbljsphdztnvjfqwrcgsmlb";
    assert_eq!(first_marker(contents), 7);
}

#[test]
fn example2() {
    let contents = "bvwbjplbgvbhsrlpgdmjqwftvncz";
    assert_eq!(first_marker(contents), 5);

}

#[test]
fn example3() {
    let contents = "nppdvjthqldpwncqszvftbrmjlhg";

    assert_eq!(first_marker(contents), 6);
}

#[test]
fn example4() {
    let contents = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg";

    assert_eq!(first_marker(contents), 10);
}


#[test]
fn example5() {
    let contents = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw";

    assert_eq!(first_marker(contents), 11);
}

