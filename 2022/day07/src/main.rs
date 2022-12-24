use std::collections::HashMap;

#[derive(Debug, Clone)]
struct File {
    parent: String,
    size: i64
}

impl File {
    fn new(parent: String, size: i64) -> Self {
        File { parent, size }
    }
}


// Full name of file/dir -> {Parent's full name, Size}
type FileSystem = HashMap<String, File>;

fn get_dir_sizes(fs: FileSystem) -> HashMap<String, i64> {
    let mut dir_sizes = HashMap::<String, i64>::new();


    // Add sizes from non-directories.
    for (_, file) in &fs {
        dir_sizes
            .entry(file.parent.to_string())
            .and_modify(|s| *s += file.size)
            .or_insert(file.size);
    }

    // Add sizes from nested directories.


    dir_sizes
}

fn get_dir_sizes_old<'a>(fs: HashMap<String, File>) -> HashMap<String, i64> {

    let mut dir_sizes = HashMap::<String, i64>::new();

    // Add sizes from non-directories.
    for (_, file) in &fs {
        dir_sizes
            .entry(file.parent.to_string())
            .and_modify(|s| *s += file.size)
            .or_insert(file.size);
    }

    // Add sizes from nested directories.
    for (name, file) in fs.clone() {
        // Get just the directories
        if file.size == 0 {
            // This is a dir.
            // Add its size to its parents.
            let this_dirs_size = *dir_sizes
                .get(&name)
                .expect(format!("{name} had 0...").as_str());
            // println!("dir {} is {}", name, this_dirs_size);

            // Add this value to its parents, all the way up to "/".
            let mut fp = name;
            // dbg!(fp);

            let mut i = 0;
            loop {
                fp = fs.get(&fp).unwrap().parent.to_string();
                // let file_to_change: &mut File = fs.get_mut(fp).unwrap();
                let file_to_change = dir_sizes.get_mut(&fp).unwrap();

                // println!("\tFile to change: {} {:?}", fp, file_to_change);
                // println!("\tAdding {}", this_dirs_size);

                *file_to_change += this_dirs_size;

                // println!("\tNew File: {} {:?}", fp, file_to_change);

                // Move the file pointer up a directory to the next parent.
                if fp == "/" { break; }
                i += 1;
                if i > 1000 {
                    panic!("Something's wrong.");
                }
                // dbg!(fp);
            }
            // println!("-------------------");
        }
    }
    dir_sizes
}


/// Make the filesystem and return it.
fn mkfs(contents: &String) -> FileSystem {
    let mut fs = FileSystem::new();
    
    // Current working directory.
    let mut full_path = Vec::<String>::new();

    for line in contents.lines() {
        // Update the cwd.
        let cwd: String = full_path.join("/");

        let tokens: Vec<_> = line.split_whitespace().collect();
        match &tokens[..] {
            ["$", "cd", loc] => {
                // 1. move up if .. and not just ["/"]
                if *loc == ".." && full_path.len() > 1 {
                    full_path.pop();
                }
                else {
                    // 2. Move there from cwd, mkdir if necessary
                    full_path.push(loc.to_string());

                    // Mkdir if it doesn't already exist
                    let new_dir_path = full_path.join("/");
                    fs.entry(new_dir_path).or_insert(File::new(cwd, 0)); // TODO verify this works as expected
                }
            },

            ["$", "ls"] => continue,

            ["dir", dirname] => {
                // Create directory at cwd
                let abs_filename = cwd.clone() + "/" + dirname;
                fs.insert(abs_filename, File::new(cwd, 0));
            },

            [filesize, filename] => {
                // Add this file at cwd.
                let abs_filename = cwd.clone() + "/" + filename;
                fs.insert(abs_filename, File::new(cwd, filesize.parse().unwrap()));
            },

            _ => unreachable!(),

        } // end of match &tokens[..]
    } // end of for line in contents.lines()

    fs
}


fn part1(contents: &String) -> i64 {
    let fs = mkfs(contents);
    dbg!(&fs);

    let sizes = get_dir_sizes(fs);
    dbg!(&sizes);

    sizes
        .values()
        .filter(|s| **s < 100_000)
        .sum()
}

fn part2(contents: &String) -> i64 {
    0
}

fn main() {
    let contents = std::fs::read_to_string("day07_input.txt").expect("Read file successfully");
    println!("Part 1: {}", part1(&contents));
    println!("Part 2: {}", part2(&contents));
}

#[test]
fn example1() {
    let contents = include_str!("../test.txt").to_string();
    assert_eq!(part1(&contents), 95437);
}

#[test]
fn example2() {

}

