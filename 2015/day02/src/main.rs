#![allow(dead_code)]
use std::fs;
use std::cmp::min;

fn surf_area(l: u32, w: u32, h: u32) -> u32 {
    let a = l * w;
    let b = w * h;
    let c = h * l;

    2 * a + 2 * b + 2 * c + min(a, min(b, c))
}

fn shortest_perim(l: u32, w: u32, h: u32) -> u32 {
    let mut nums = vec![l, w, h];
    nums.sort();
    nums.remove(2);

    let extra = l * w * h;

    nums.iter().sum::<u32>() * 2 + extra
}

fn main() {
    let filepath = "day02_input.txt";
    let contents = fs::read_to_string(filepath).expect("Read successfully");

    let mut total_paper = 0;
    let mut total_ribbon = 0;

    for line in contents.lines() {
        let nums = 
            line.split("x")
            .map(|s| s.parse().unwrap())
            .take(3)
            .collect::<Vec<u32>>();

        if let [l, w, h] = nums[..] {
            total_paper += surf_area(l, w, h);
            total_ribbon += shortest_perim(l, w, h);
        }

    }

    println!("total paper: {total_paper}");
    println!("total ribbon: {total_ribbon}");
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

#[test]
fn test_ribbon1() {
    let feet = shortest_perim(2, 3, 4);
    assert_eq!(feet, 34);
}

#[test]
fn test_ribbon2() {
    let feet = shortest_perim(1, 1, 10);
    assert_eq!(feet, 14);
}
