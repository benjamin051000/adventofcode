#![allow(unused_variables)]

mod fs;

fn part1(contents: &String) -> i32 {
    // Make root node
    let mut filesys: fs::File<String> = fs::File::new("/".to_string(), fs::FileType::mkdir());
    let fp = &mut filesys;

    for line in contents.lines() {
        // dbg!(line.split(" ").collect::<Vec<&str>>());

        let tokens: Vec<_> = line.split_whitespace().collect();
        match &tokens[..] {
            ["$", "cd", loc] => {
                println!("Going to {loc}");
                // Attempt to "cd" into this dir. If it doesn't exist, make it first.
                // 1. Are we already at loc?
                if *loc == fp.name {
                    continue;
                }
                else if *loc == ".." {
                    // Go up a directory. 
                    todo!();
                }

                // 2. Check if loc exists.

                
            }

            ["$", "ls"] => continue,

            ["dir", dirname] => {
                fp.add(
                    fs::File::new(
                        dirname.to_string(),
                        fs::FileType::mkdir()
                    )
                ).unwrap();
            }

            [size, name] => {
                // Add this file to current dir.
                let s = size.parse::<usize>().unwrap();
                fp.add(
                    fs::File::new(
                        name.to_string(),
                        fs::FileType::touch(
                            s, 
                            String::new()
                        )
                    )
                ).unwrap();
            }
            _ => unreachable!()
        }
    }

    dbg!(filesys);

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

