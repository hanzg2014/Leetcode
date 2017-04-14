//second trial

class Solution {
public:
    
    vector<int> sequence(vector<int> &nums1){
            int k;
            for(int i = 0; i < nums1.size() - 1; i++){
                for (int j = i + 1; j < nums1.size(); j++){
                    if (nums1[i] > nums1[j]){
                        k = nums1[i];
                        nums1[i] = nums1[j];
                        nums1[j] = k;
                   }
                }
            }
            return nums1;
         }
    
    bool ifExist(vector<vector<int>> v_list, vector<int> v){
            for(auto v1 : v_list){
                if (v1 == v)
                    return true;
            }
            return false;
        }
        
    vector<vector<int>> threeSum(vector<int>& nums) {
        
        nums = sequence(nums);
        vector<vector<int>> v_list;
    
        for(int i = 0; i < nums.size() - 2; i++){
            for(int j = i + 1; j < nums.size() - 1; j++){
                for(int k = j + 1; k < nums.size(); k++){
                    if ((nums[i] + nums[j] + nums[k]) == 0){
                          if(!ifExist(v_list, {nums[i],nums[j],nums[k]}))
                          v_list.push_back({nums[i],nums[j],nums[k]});
                          break;
                    }
                }
            }
            
        }
        return v_list;
    }
};

//Exceeding Time Limit (with no doubt)
//2016年10月31日 19:38
