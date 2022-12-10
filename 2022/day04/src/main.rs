#[derive(Debug)]
struct Range(i32, i32);


/// Check if Range a partially overlaps with Range b.
fn partial_overlap(a: &Range, b: &Range) -> bool {
    use std::cmp::{max, min};

    let lo = max(a.0, b.0);
    let hi = min(a.1, b.1);

    lo <= hi // Are bounds valid? If so, they overlap.
}


/// Check if Range a fully contains Range b.
fn full_overlap(a: &Range, b: &Range) -> bool {
    (a.0 <= b.0 && a.1 >= b.1) || (b.0 <= a.0 && b.1 >= a.1)
}


fn get_ranges<'a>(line: &'a str) -> [Range; 2] {
    // Get pairs
    // Left and Right Low and High
    let [ll, lh, rl, rh]: [i32; 4] = line
        .split(['-',','])
        .map(|s| s.parse())
        .collect::<Result<Vec<_>, _>>() // Stops after first Err
        .unwrap()
        .try_into()
        .unwrap();

    let a = Range(ll, lh);
    let b = Range (rl, rh);

    // Ensure ranges are valid.
    assert!(a.0 <= a.1);
    assert!(b.0 <= b.1);

    [a, b]
}


fn part1(contents: &String) -> i32 {

    let mut total = 0;

    for line in contents.lines() {
        
        let [a, b] = get_ranges(line);

        if full_overlap(&a, &b) {
            println!("{:?} is fully contained in {:?}", &a, &b);
            total += 1;
        }
    }

    total
}


fn part2(contents: &String) -> i32 {
    let mut total = 0;

    for line in contents.lines() {
        
        let [a, b] = get_ranges(line);

        if partial_overlap(&a, &b) {
            println!("{a:?} and {b:?} partially overlap.");
            total += 1;
        }

    }

    total
}


fn main() {
    let contents = std::fs::read_to_string("day04_input.txt").expect("Read file successfully");
    println!("Part 1: {}", part1(&contents));
    println!("Part 2: {}", part2(&contents));
}


#[test]
fn example1() {
    let contents = "2-4,6-8\n\
                    2-3,4-5\n\
                    5-7,7-9\n\
                    2-8,3-7\n\
                    6-6,4-6\n\
                    2-6,4-8".to_string();

    assert_eq!(part1(&contents), 2);
}


#[test]
fn example2() {
    let contents = "2-4,6-8\n\
                    2-3,4-5\n\
                    5-7,7-9\n\
                    2-8,3-7\n\
                    6-6,4-6\n\
                    2-6,4-8".to_string();

    assert_eq!(part2(&contents), 4);
}
