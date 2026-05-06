import requests

def get_github_repo_stars(owner, repo):
    """
    获取 GitHub 仓库的 star 数量

    Args:
        owner (str): 仓库所有者
        repo (str): 仓库名称

    Returns:
        int: star 数量
    """
    url = f"https://api.github.com/repos/{owner}/{repo}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功

        repo_data = response.json()
        stars = repo_data.get('stargazers_count', 0)

        return stars

    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return None
    except ValueError as e:
        print(f"JSON 解析失败: {e}")
        return None

if __name__ == "__main__":
    owner = "NousResearch"
    repo_name = "hermes-agent"

    stars = get_github_repo_stars(owner, repo_name)

    if stars is not None:
        print(f"仓库 {owner}/{repo_name} 的 star 数量: {stars}")
    else:
        print("获取 star 数量失败")