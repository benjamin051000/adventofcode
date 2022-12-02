use std::fs;

const THEM_ROCK: &str = "A";
const THEM_PAPER: &str = "B";
const THEM_SCISSORS: &str = "C";

const YOU_ROCK: &str = "X"; // No, you do! <3
const YOU_PAPER: &str = "Y";
const YOU_SCISSORS: &str = "Z";

fn score_round(your_shape: &str, their_shape: &str) -> i32 {
    // dbg!(&your_shape, &their_shape);

    let shape_score = match your_shape {
        YOU_ROCK => 1,
        YOU_PAPER => 2,
        YOU_SCISSORS => 3,
        _ => unreachable!(),
    };

    // dbg!(&shape_score);

    // If you won, +3
    let win_bonus = match (their_shape, your_shape) {
        // You won
        (THEM_ROCK, YOU_PAPER) => 6,
        (THEM_PAPER, YOU_SCISSORS) => 6,
        (THEM_SCISSORS, YOU_ROCK) => 6,
        // You lost
        (THEM_ROCK, YOU_SCISSORS) => 0,
        (THEM_PAPER, YOU_ROCK) => 0,
        (THEM_SCISSORS, YOU_PAPER) => 0,
        // Draw
        _ => 3,
    };

    // dbg!(&win_bonus);

    shape_score + win_bonus
}

fn score_game(game: &String) -> i32 {
    let mut sum = 0;
    for round in game.lines() {
        // lines are guaranteed to be "A B" where A and B are one char
        // separated by a space
        let (theirs, yours) = round.split_once(' ').unwrap();
        sum += score_round(yours, theirs);
    }
    sum
}

fn pick_shape<'a>(theirs: &'a str, strategy: &'a str) -> &'a str {
    const LOSE: &str = "X";
    const DRAW: &str = "Y";
    const WIN: &str = "Z";
    match (theirs, strategy) {
        (THEM_ROCK, LOSE) => YOU_SCISSORS,
        (THEM_ROCK, DRAW) => YOU_ROCK,
        (THEM_ROCK, WIN) => YOU_PAPER,

        (THEM_PAPER, LOSE) => YOU_ROCK,
        (THEM_PAPER, DRAW) => YOU_PAPER,
        (THEM_PAPER, WIN) => YOU_SCISSORS,

        (THEM_SCISSORS, LOSE) => YOU_PAPER,
        (THEM_SCISSORS, DRAW) => YOU_SCISSORS,
        (THEM_SCISSORS, WIN) => YOU_ROCK,

        _ => unreachable!(),
    }
}

fn actual_strategy(game: &String) -> i32 {
    let mut sum = 0;
    for round in game.lines() {
        // lines are guaranteed to be "A B" where A and B are one char
        // separated by a space
        let (theirs, strategy) = round.split_once(' ').unwrap();
        let yours = pick_shape(theirs, strategy);
        sum += score_round(yours, theirs);
    }
    sum
}

fn main() {
    let contents = fs::read_to_string("day02_input.txt").expect("Read file successfully");
    println!("Part 1: {}", score_game(&contents));
    println!("Part 2: {}", actual_strategy(&contents));
}

#[test]
fn example1() {
    let contents = String::from(
        "A Y
B X
C Z
",
    );

    assert_eq!(score_game(&contents), 15);
}

#[test]
fn example2() {
    let contents = String::from(
        "A Y
B X
C Z
",
    );

    assert_eq!(actual_strategy(&contents), 12);
}
