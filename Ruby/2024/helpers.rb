module Helpers
  def open_input_file(file_path)
    File.open(file_path, 'r') do |f|
      f.readlines.map(&:chomp)
    end
  end
end