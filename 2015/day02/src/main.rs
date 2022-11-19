#![allow(dead_code)]
use std::fs;
use std::cmp::min;

fn surf_area(l: u32, w: u32, h: u32) -> u32 {
    let a = l * w;
    let b = w * h;
    let c = h * l;

    2 * a + 2 * b + 2 * c + min(a, min(b, c))
}

fn main() {
    let filepath = "day02_input.txt";
    let contents = fs::read_to_string(filepath).expect("Read successfully");

    let mut total = 0;

    for line in contents.lines() {
        let nums = 
            line.split("x")
            .map(|s| s.parse().unwrap())
            .take(3)
            .collect::<Vec<u32>>();

        if let [l, w, h] = nums[..] {
            total += surf_area(l, w, h);
        }

    }

    println!("total: {total}");
}

#[test]
fn tc1() {
    let area = surf_area(2, 3, 4);
    assert_eq!(area, 58);
}

#[test]
fn test() {
    let area = surf_area(1, 1, 10);
    assert_eq!(area, 43);
}
