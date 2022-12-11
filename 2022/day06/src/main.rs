fn all_unique(elements: &[char]) -> bool {
    let mut h = std::collections::HashSet::new();
    for e in elements {
        if !h.insert(e) {
            return false;
        }
    }

    true
}

fn first_marker(stream: &str, num_unique: usize) -> u32 {
    for (idx, window) in stream.chars().collect::<Vec<char>>().windows(num_unique).enumerate() {
        // Check if each of the fours are unique
        // if they are all different, then a != b && b != c && c != d
        if  all_unique(window) {
            return (idx + num_unique) as u32; // idx of first marker char + 4 = idx of ending marker char
        }
    }

    unreachable!();
}

fn part1(contents: &String) -> u32 {
    first_marker(contents, 4)
}

fn part2(contents: &String) -> u32 {
    first_marker(contents, 14)
}

fn main() {
    let contents = std::fs::read_to_string("day06_input.txt").expect("Read file successfully");
    println!("Part 1: {}", part1(&contents));
    println!("Part 2: {}", part2(&contents));
}

#[test]
fn example1() {
    let contents = "mjqjpqmgbljsphdztnvjfqwrcgsmlb";
    assert_eq!(first_marker(contents, 4), 7);
    assert_eq!(first_marker(contents, 14), 19);
}

#[test]
fn example2() {
    let contents = "bvwbjplbgvbhsrlpgdmjqwftvncz";
    assert_eq!(first_marker(contents, 4), 5);
    assert_eq!(first_marker(contents, 14), 23);

}

#[test]
fn example3() {
    let contents = "nppdvjthqldpwncqszvftbrmjlhg";

    assert_eq!(first_marker(contents, 4), 6);
    assert_eq!(first_marker(contents, 14), 23);
}

#[test]
fn example4() {
    let contents = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg";

    assert_eq!(first_marker(contents, 4), 10);
    assert_eq!(first_marker(contents, 14), 29);
}


#[test]
fn example5() {
    let contents = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw";

    assert_eq!(first_marker(contents, 4), 11);
    assert_eq!(first_marker(contents, 14), 26);
}

