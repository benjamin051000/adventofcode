use std::fs;
use std::collections::HashMap;

fn one_santa(contents: &String) -> u32 {
    let mut x = 0;
    let mut y  = 0;
    let mut map = HashMap::new();
    map.insert((x, y), 1); // Give first present

    for c in contents.chars() {
        match c {
            '>' => x += 1,
            'v' => y += 1, // inverted y
            '<' => x -= 1,
            '^' => y -= 1,
            invalid => panic!("Invalid char: '{invalid}'")
        }

        // Drop present here
        let num_presents = map.entry((x, y)).or_insert(1);
        *num_presents += 1;
    }

   map.keys().len() as u32
}

fn two_santas(contents: &String) -> u32 {
    let mut x1 = 0;
    let mut y1 = 0;

    let mut x2  = 0;
    let mut y2  = 0;

    let mut map = HashMap::new();
    map.insert((x1, y1), 2); // Give first present

    // Santa 1
    for c in contents.chars().step_by(2) {
        match c {
            '>' => x1 += 1,
            'v' => y1 += 1, // inverted y
            '<' => x1 -= 1,
            '^' => y1 -= 1,
            invalid => panic!("Invalid char: '{invalid}'")
        }

        // Drop present here
        let num_presents = map.entry((x1, y1)).or_insert(1);
        *num_presents += 1;
    }

    // Santa 2
    for c in contents.chars().skip(1).step_by(2) {
        match c {
            '>' => x2 += 1,
            'v' => y2 += 1, // inverted y
            '<' => x2 -= 1,
            '^' => y2 -= 1,
            invalid => panic!("Invalid char: '{invalid}'")
        }

        // Drop present here
        let num_presents = map.entry((x2, y2)).or_insert(1);
        *num_presents += 1;
    }

   map.keys().len() as u32
}

fn main() {
    let filepath = "day03_input.txt";
    let contents = fs::read_to_string(filepath).expect("Read input file successfully");

    println!("Single santa delivered to {} houses", one_santa(&contents));
    println!("Two santas delivered to {} houses", two_santas(&contents));
}
