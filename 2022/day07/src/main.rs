#![allow(unused_variables)]

mod fs;

fn part1(contents: &String) -> i32 {
    // Make root node
    let mut filesys: fs::File<String> = fs::File::new("/".to_string(), fs::FileType::mkdir());

    for line in contents.lines() {
        // dbg!(line.split(" ").collect::<Vec<&str>>());

        let tokens: Vec<_> = line.split_whitespace().collect();
        match &tokens[..] {
            ["$", "cd", loc] => println!("Going to {loc}"),
            ["$", "ls"] => println!("ls"),
            ["dir", dirname] => println!("mkdir {dirname}"),
            other => println!("{:?}", other)
        }
    }

    0
}

fn part2(contents: &String) -> i32 {
    0
}

fn main() {
    let contents = std::fs::read_to_string("day04_input.txt").expect("Read file successfully");
    println!("Part 1: {}", part1(&contents));
    println!("Part 2: {}", part2(&contents));
}

#[test]
fn example1() {
    let contents = include_str!("../test.txt").to_string();

    dbg!(&contents);
    part1(&contents);
    assert!(false);

}

#[test]
fn example2() {

}

