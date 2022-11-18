use std::fs;

fn main() {

    let filepath = "day01_input.txt";
    let contents = fs::read_to_string(filepath).expect("Should have beeen able to read the file");

    let mut current_floor = 0;
    let mut check_basement = true;
    let mut first_basement = 1;

    for (i, c) in contents.chars().enumerate() {

        match c {
            '(' => current_floor += 1,
            ')' => current_floor -= 1,
            invalid => println!("Skipping invalid character \"{invalid}\" ")
        }

        if check_basement && current_floor < 0 {
            check_basement = false;
            first_basement = i+1;
        }
    }

    println!("Final floor: {current_floor}");
    println!("First basement: {first_basement}");
}
