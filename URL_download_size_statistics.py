import requests
import time
import random

# 伪装成浏览器的headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    # 其他headers...
}

def get_url_size(url):
    try:
        # 发送HEAD请求以获取头部信息
        response_head = requests.head(url, headers=headers, allow_redirects=True)
        
        # 检查Retry-After头部
        if response_head.status_code == 429:
            retry_after = int(response_head.headers.get('Retry-After', 60))  # 默认60秒
            print(f"Too Many Requests. Retrying after {retry_after} seconds...")
            time.sleep(retry_after)
            return get_url_size(url)  # 递归调用，尊重Retry-After
        
        # 如果HEAD请求成功且包含Content-Length头部，则直接返回内容长度
        if response_head.status_code == 200 and 'content-length' in response_head.headers:
            return int(response_head.headers['content-length'])
        
        # 如果HEAD请求没有返回Content-Length头部，则发送GET请求下载文件并计算大小
        response_get = requests.get(url, headers=headers, stream=True)
        if response_get.status_code == 200:
            return len(response_get.content)
        else:
            print(f"Failed to retrieve {url}. Status code: {response_get.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def main():
    total_size = 0
    with open('urls.txt', 'r') as file:
        for line in file:
            url = line.strip()  # 移除可能的空白字符
            if url:  # 确保URL不为空
                size = get_url_size(url)
                if size is not None:
                    total_size += size
                    print(f"URL: {url}, Size: {size} bytes")
        
        # 在请求之间添加随机延迟，以减少触发速率限制的可能性
        time.sleep(random.uniform(1, 3))

    print(f"Total size of all URLs: {total_size} bytes")

if __name__ == "__main__":
    main()