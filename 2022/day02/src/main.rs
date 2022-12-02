use std::fs;

fn main() {
    let contents = fs::read_to_string("day02_input.txt").expect("Read file successfully");
    println!("Part 1: {}", score_game(&contents));
}

fn score_round(your_shape: &str, their_shape: &str) -> i32 {
    dbg!(&your_shape, &their_shape);

    let shape_score = match your_shape {
        "X" => 1,
        "Y" => 2,
        "Z" => 3,
            _ => unreachable!()
    };

    // dbg!(&shape_score);

    // If you won, +3
    let win_bonus = match (their_shape, your_shape) {
        // You won
        ("A", "Y") => 6,
        ("B", "Z") => 6,
        ("C", "X") => 6,
        // You lost
        ("A", "Z") => 0,
        ("B", "X") => 0,
        ("C", "Y") => 0,
        // Draw
        _ => 3
    };

    // dbg!(&win_bonus);

    shape_score + win_bonus
}

fn score_game(game: &String) -> i32 {
    let mut sum = 0;
    for round in game.lines() {
        // lines are guaranteed to be "A B" where A and B are one char
        // separated by a space
        let (theirs, yours) = round.split_once(" ").unwrap();
        sum += score_round(yours, theirs);
        
    }
    sum
}

#[test]
fn example() {
    let contents = String::from(
        "A Y
B X
C Z
");

    assert_eq!(score_game(&contents), 15);
}
