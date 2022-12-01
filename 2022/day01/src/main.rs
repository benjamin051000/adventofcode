use std::fs::read_to_string;

fn parse(contents: &String) -> Vec<i32> {
    let mut result = vec![0];
    let mut i = 0;
    
    for line in contents.lines() {
        match line {
            "" => {
                i += 1;
                result.push(0);
            }
            _ => result[i] += line.parse::<i32>().unwrap(),
        }
    }

    result
}

fn max_calories(v: Vec<i32>) -> i32 {
    *v.iter().max().unwrap()
}

fn top_three(v: &mut Vec<i32>) -> i32 {
    v.sort();
    v.reverse();
    v.iter().take(3).sum::<i32>()
}

fn main() {
    let contents = read_to_string("./day01_input.txt").expect("Input loaded successfully");
    println!("Part 1: {}", max_calories(parse(&contents)));
    println!("Part 2: {:?}", top_three(&mut parse(&contents)));
}


#[test]
fn example1() {
    let contents = String::from("1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
");

    assert_eq!(max_calories(parse(&contents)), 24000);
    assert_eq!(top_three(&mut parse(&contents)), 45000);
}


