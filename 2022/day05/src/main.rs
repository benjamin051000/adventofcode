use std::collections::LinkedList;
type Stack<T> = LinkedList<T>;

fn parse_into_stacks(contents: String) -> Vec<Stack<char>> {
    let mut v2 = Vec::<Vec<char>>::new();

    for line in contents.lines() {
        // Stop at the first empty line.
        if line.is_empty() {
            break;
        }

        v2.push(line.chars().collect());
    }

    // Now, convert it to a vec of stacks, where each 
    // stack is a column in the original 2d vec
    let mut result = Vec::<Stack<char>>::new();

    // For each column
    for col in 0..v2[0].len() {
        let mut stack = Stack::<char>::new();

        // For each row
        for row in 0..v2.len() {
            let c = v2[row][col];

            // only allow Letters and Numbers
            if c.is_alphanumeric() {
                // Add the number to the stack
                stack.push_back(c);
            }
        } // end of r,c loops

        // Some stacks will be empty if it wasn't a col with numbers. 
        if !stack.is_empty() {
            result.push(stack);
        }

    }

    result
}

fn process_moves(mut stacks: Vec<Stack<char>>, moves: std::str::Lines, reverse: bool) -> Vec<Stack<char>> {
    for m in moves {
        // Parse n, to, from
        let [n, from, to]: [usize; 3] = m
            .split(' ')
            .filter_map(|s| s.parse().ok())
            .collect::<Vec<_>>()
            .try_into()
            .unwrap();

        dbg!(n, from, to);

        // Move the stacks
        if !reverse {
            // Part 1
            for _ in 1..=n {
                let f = stacks[from-1].pop_front().unwrap();
                stacks[to-1].push_front(f);
            }
        }
        else {
            let mut temp = Stack::<char>::new();

            // Dump into temp
            for _ in 1..=n {
                let f = stacks[from-1].pop_front().unwrap();
                temp.push_front(f);
            }

            // Move from temp to dest, which will reverse the order
            for _ in 1..=n {
                let cargo_box = temp.pop_front().unwrap();
                stacks[to-1].push_front(cargo_box);
            }

        }
        dbg!(&stacks);

    }

    stacks
}

fn part1(contents: &String) -> String {
    // Split contents into stack half and move half
    let [stack_text, move_text]: [&str; 2] = contents
        .split("\n\n")
        .collect::<Vec<_>>()
        .try_into()
        .unwrap();

    let stacks = parse_into_stacks(stack_text.to_string());

    dbg!(&stacks);

    let stacks = process_moves(stacks, move_text.to_string().lines(), false);

    // Get all the top of the stacks
    let tops = stacks
        .iter()
        .filter_map(|s| s.front())
        .collect::<Vec<&char>>();

    String::from_iter(tops)
}

fn part2(contents: &String) -> String {

    // Split contents into stack half and move half
    let [stack_text, move_text]: [&str; 2] = contents
        .split("\n\n")
        .collect::<Vec<_>>()
        .try_into()
        .unwrap();

    let stacks = parse_into_stacks(stack_text.to_string());

    dbg!(&stacks);

    let stacks = process_moves(stacks, move_text.to_string().lines(), true);

    // Get all the top of the stacks
    let tops = stacks
        .iter()
        .filter_map(|s| s.front())
        .collect::<Vec<&char>>();

    String::from_iter(tops)
}

fn main() {
    let contents = std::fs::read_to_string("day05_input.txt").expect("Read file successfully");
    println!("Part 1: {}", part1(&contents));
    println!("Part 2: {}", part2(&contents));
}

#[test]
fn example1() {
    let contents = include_str!("../example1.txt").to_string();

    let result = "CMZ";

    assert_eq!(part1(&contents), result);
}

#[test]
fn example2() {
    let contents = include_str!("../example1.txt").to_string();

    let result = "MCD";

    assert_eq!(part2(&contents), result);
}

