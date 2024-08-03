use day09::*;
use std::collections::HashSet;

fn part1(contents: &String) -> u32 {
    let mut visited: HashSet<Coord> = HashSet::new();

    // Remember, 0,0 is bottom left, NOT top left. TODO this may not even matter anyway
    let mut head: Coord = (0, 0);
    let mut tail: Coord = (0, 0);

    for line in contents.lines() {
        let tokens: Vec<&str> = line.split_whitespace().collect();
        let (dir, num) = if let [d, n] = tokens[..] {
            (d, n.parse::<i32>().unwrap())
        } else {
            unreachable!();
        };

        dbg!(&tokens);
        dbg!(&(dir, num));

        match dir {
            "U" => {
                head.0 += num;
            }

            "D" => {
                head.0 -= num;
            }

            "L" => {
                head.1 -= num;
            }

            "R" => {
                head.1 += num;
            }

            _ => unreachable!(),
        } // end of match &tokens[..]

        dbg!(&head);

        // Now, update the tail if head is too far away.
        move_tail(&mut tail, &head);
    } // end of for line in contents.lines()

    visited.len() as u32
}

fn part2(contents: &String) -> i32 {
    todo!();
}

fn main() {
    let contents = std::fs::read_to_string("day09_input.txt").expect("Read file successfully");
    println!("Part 1: {}", part1(&contents));
    println!("Part 2: {}", part2(&contents));
}

#[test]
fn example1() {
    let contents = include_str!("../test.txt").to_string();
    assert_eq!(part1(&contents), 13);
}

#[test]
fn example2() {}
